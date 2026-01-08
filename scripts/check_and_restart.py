#!/usr/bin/env python3
"""
Simple check and restart script - run this periodically
"""

import subprocess
import os
import json
import sys
from datetime import datetime, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRAPER_SCRIPT = os.path.join(SCRIPT_DIR, "browser_op_scraper.py")
PROGRESS_FILE = os.path.join(SCRIPT_DIR, "..", "browser_scrape_progress.json")
STUCK_THRESHOLD = 1800  # 30 minutes

def check_and_restart():
    """Check scraper status and restart if needed"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Checking scraper...")
    
    # Check if progress file exists and is recent
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                last_index = data.get('last_index', 0)
                last_updated_str = data.get('last_updated', '')
                
                # Parse timestamp
                try:
                    last_updated = datetime.fromisoformat(last_updated_str.replace('Z', '+00:00'))
                    if last_updated.tzinfo is None:
                        last_updated = datetime.fromisoformat(last_updated_str)
                except:
                    last_updated = datetime.fromtimestamp(os.path.getmtime(PROGRESS_FILE))
                
                age = (datetime.now() - last_updated).total_seconds()
                age_min = age / 60
                
                print(f"  Progress: {last_index}/1340 ops ({last_index*100/1340:.1f}%)")
                print(f"  Last update: {age_min:.1f} minutes ago")
                
                if age > STUCK_THRESHOLD:
                    print(f"  [WARN] Scraper appears stuck (no progress in {age_min:.1f} min)")
                    print(f"  [INFO] Restarting with --resume...")
                    restart_scraper()
                    return
                else:
                    print(f"  [OK] Scraper making progress")
                    return
                    
        except Exception as e:
            print(f"  [WARN] Error reading progress: {e}")
    
    # No progress file or error - check if process is running
    try:
        result = subprocess.run(
            ['powershell', '-Command', 'Get-Process python -ErrorAction SilentlyContinue | Measure-Object | Select-Object -ExpandProperty Count'],
            capture_output=True,
            text=True,
            timeout=10
        )
        count = int(result.stdout.strip() or '0')
        
        if count == 0:
            print(f"  [WARN] No Python processes running")
            print(f"  [INFO] Starting scraper...")
            restart_scraper()
        else:
            print(f"  [INFO] Python process(es) running ({count}), but no progress file yet")
            print(f"  [INFO] Waiting for first progress save (every 10 ops)...")
    except Exception as e:
        print(f"  [ERROR] Could not check processes: {e}")

def restart_scraper():
    """Restart the scraper"""
    print(f"  Starting: python {SCRAPER_SCRIPT} --resume")
    subprocess.Popen(
        [sys.executable, SCRAPER_SCRIPT, '--resume'],
        cwd=SCRIPT_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    print(f"  [OK] Scraper started in background")

if __name__ == "__main__":
    check_and_restart()






