#!/usr/bin/env python3
"""
Monitor and auto-restart scraper

Periodically checks if scraper is running and making progress.
Restarts with --resume if it's stuck or crashed.
"""

import subprocess
import time
import os
import json
import sys
from datetime import datetime, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRAPER_SCRIPT = os.path.join(SCRIPT_DIR, "browser_op_scraper.py")
PROGRESS_FILE = os.path.join(SCRIPT_DIR, "..", "browser_scrape_progress.json")
CHECK_INTERVAL = 300  # Check every 5 minutes
STUCK_THRESHOLD = 1800  # Consider stuck if no progress in 30 minutes
TOTAL_OPS = 1340  # Approximate total

def get_last_progress():
    """Get the last saved progress"""
    if not os.path.exists(PROGRESS_FILE):
        return None, None
    
    try:
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            last_index = data.get('last_index', 0)
            last_updated_str = data.get('last_updated', '')
            
            try:
                last_updated = datetime.fromisoformat(last_updated_str.replace('Z', '+00:00'))
                if last_updated.tzinfo is None:
                    # Handle naive datetime
                    last_updated = datetime.fromisoformat(last_updated_str)
            except:
                # Fallback: use file modification time
                last_updated = datetime.fromtimestamp(os.path.getmtime(PROGRESS_FILE))
            
            return last_index, last_updated
    except Exception as e:
        print(f"[WARN] Error reading progress: {e}")
        return None, None

def is_scraper_running():
    """Check if scraper process is running by checking progress file modification"""
    # Simple heuristic: if progress file was modified recently (within last hour), assume it's running
    if os.path.exists(PROGRESS_FILE):
        file_time = datetime.fromtimestamp(os.path.getmtime(PROGRESS_FILE))
        age = (datetime.now() - file_time).total_seconds()
        return age < 3600  # Modified within last hour
    
    # Also try to check Python processes as fallback
    try:
        result = subprocess.run(
            ['powershell', '-Command', "Get-Process python -ErrorAction SilentlyContinue | Measure-Object | Select-Object -ExpandProperty Count"],
            capture_output=True,
            text=True,
            timeout=10
        )
        count = int(result.stdout.strip() or '0')
        return count > 0
    except:
        return False

def restart_scraper():
    """Restart the scraper with --resume"""
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Restarting scraper with --resume...")
    print("-" * 60)
    
    process = subprocess.Popen(
        [sys.executable, SCRAPER_SCRIPT, '--resume'],
        cwd=SCRIPT_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        encoding='utf-8',
        errors='replace'
    )
    
    return process

def monitor_loop():
    """Main monitoring loop"""
    last_check_index = None
    last_check_time = None
    process = None
    
    print("=" * 60)
    print("Scraper Monitor - Auto Restart")
    print("=" * 60)
    print(f"Check interval: {CHECK_INTERVAL // 60} minutes")
    print(f"Stuck threshold: {STUCK_THRESHOLD // 60} minutes")
    print("=" * 60)
    print()
    
    # Initial check - start scraper if not running
    if not is_scraper_running():
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Scraper not running. Starting...")
        process = restart_scraper()
    else:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Scraper appears to be running.")
    
    while True:
        try:
            time.sleep(CHECK_INTERVAL)
            
            current_time = datetime.now()
            print(f"\n[{current_time.strftime('%H:%M:%S')}] Checking scraper status...")
            
            # Check progress
            current_index, last_updated = get_last_progress()
            
            if current_index is not None:
                progress_pct = (current_index / TOTAL_OPS) * 100
                print(f"  Progress: {current_index}/{TOTAL_OPS} ops ({progress_pct:.1f}%)")
                
                if last_updated:
                    age = current_time - last_updated
                    print(f"  Last update: {age.total_seconds() / 60:.1f} minutes ago")
                    
                    # Check if stuck
                    if age.total_seconds() > STUCK_THRESHOLD:
                        print(f"  [WARN] Scraper appears stuck (no progress in {age.total_seconds() / 60:.1f} min)")
                        if is_scraper_running():
                            print("  [INFO] Killing stuck process...")
                            try:
                                subprocess.run(['powershell', '-Command', 'Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force'], timeout=10)
                                time.sleep(5)
                            except:
                                pass
                        print("  [INFO] Restarting...")
                        process = restart_scraper()
                        last_check_index = current_index
                        last_check_time = current_time
                        continue
                    
                    # Check if progress is being made
                    if last_check_index is not None and current_index == last_check_index:
                        print(f"  [INFO] No new progress since last check")
                    elif last_check_index is not None:
                        ops_per_min = (current_index - last_check_index) / (CHECK_INTERVAL / 60)
                        print(f"  [INFO] Progress rate: {ops_per_min:.2f} ops/min")
                    
                    last_check_index = current_index
                    last_check_time = current_time
                else:
                    print(f"  [INFO] Progress file exists but no timestamp")
            else:
                print(f"  [INFO] No progress file yet (still initializing or first run)")
            
            # Check if process is running
            running = is_scraper_running()
            if not running:
                print(f"  [WARN] Scraper process not detected")
                print(f"  [INFO] Restarting...")
                process = restart_scraper()
            else:
                print(f"  [OK] Scraper process is running")
                
            # Check if we're done
            if current_index and current_index >= TOTAL_OPS:
                print(f"\n{'='*60}")
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Scraping appears complete!")
                print(f"Final progress: {current_index}/{TOTAL_OPS} ops")
                print("=" * 60)
                break
                
        except KeyboardInterrupt:
            print(f"\n\n[{datetime.now().strftime('%H:%M:%S')}] Monitor stopped by user")
            break
        except Exception as e:
            print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Error in monitor: {e}")
            print("Continuing...")
            time.sleep(60)  # Wait a bit before retrying

if __name__ == "__main__":
    try:
        monitor_loop()
    except KeyboardInterrupt:
        print("\n\nMonitor stopped.")

