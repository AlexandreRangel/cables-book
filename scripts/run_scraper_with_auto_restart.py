#!/usr/bin/env python3
"""
Auto-restart wrapper for browser_op_scraper.py

This script monitors and automatically restarts the scraper if it crashes or gets stuck.
It will keep running until all ops are scraped.
"""

import subprocess
import time
import os
import json
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROGRESS_FILE = os.path.join(SCRIPT_DIR, "..", "browser_scrape_progress.json")
SCRAPER_SCRIPT = os.path.join(SCRIPT_DIR, "browser_op_scraper.py")
MAX_RESTARTS = 100
STUCK_TIMEOUT = 1800  # 30 minutes - if no progress in 30 min, consider stuck

def get_last_progress():
    """Get the last saved progress index"""
    if not os.path.exists(PROGRESS_FILE):
        return None
    
    try:
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('last_index', None)
    except:
        return None

def check_if_stuck(last_index, last_check_time):
    """Check if scraper appears to be stuck"""
    current_index = get_last_progress()
    
    if current_index is None:
        # No progress file yet, not stuck
        return False, current_index
    
    if current_index == last_index:
        # No progress made
        elapsed = time.time() - last_check_time
        if elapsed > STUCK_TIMEOUT:
            return True, current_index
    else:
        # Progress made, reset timer
        return False, current_index
    
    return False, current_index

def run_scraper(restart_count=0):
    """Run the scraper and monitor it"""
    print(f"\n{'='*60}")
    print(f"Starting scraper (restart #{restart_count})")
    print(f"{'='*60}\n")
    
    last_index = get_last_progress()
    last_check_time = time.time()
    
    # Run scraper
    process = subprocess.Popen(
        ['python', SCRAPER_SCRIPT, '--resume'],
        cwd=SCRIPT_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        encoding='utf-8',
        errors='replace'
    )
    
    # Monitor output
    try:
        for line in process.stdout:
            print(line.rstrip())
            
            # Check for progress updates every 5 minutes
            if time.time() - last_check_time > 300:  # 5 minutes
                stuck, new_index = check_if_stuck(last_index, last_check_time)
                
                if stuck:
                    print(f"\n[WARN] Scraper appears stuck (no progress in {STUCK_TIMEOUT//60} min)")
                    print(f"[WARN] Last index: {last_index}, Current index: {new_index}")
                    print("[WARN] Restarting scraper...\n")
                    process.terminate()
                    process.wait(timeout=10)
                    return 'stuck', restart_count + 1
                
                last_index = new_index
                last_check_time = time.time()
        
        # Process finished
        return_code = process.wait()
        
        if return_code == 0:
            print("\n[SUCCESS] Scraper completed successfully!")
            return 'completed', restart_count
        else:
            print(f"\n[ERROR] Scraper exited with code {return_code}")
            return 'error', restart_count + 1
            
    except KeyboardInterrupt:
        print("\n[INFO] Interrupted by user")
        process.terminate()
        process.wait(timeout=10)
        return 'interrupted', restart_count
    except Exception as e:
        print(f"\n[ERROR] Exception: {e}")
        process.terminate()
        try:
            process.wait(timeout=10)
        except:
            pass
        return 'exception', restart_count + 1

def main():
    """Main monitoring loop"""
    restart_count = 0
    
    print("="*60)
    print("Browser Op Scraper - Auto-Restart Monitor")
    print("="*60)
    print(f"Monitor will restart scraper if it crashes or gets stuck")
    print(f"Stuck timeout: {STUCK_TIMEOUT//60} minutes")
    print(f"Max restarts: {MAX_RESTARTS}")
    print("="*60)
    
    while restart_count < MAX_RESTARTS:
        status, restart_count = run_scraper(restart_count)
        
        if status == 'completed':
            print("\n" + "="*60)
            print("ALL DONE! Scraping completed successfully.")
            print("="*60)
            break
        elif status == 'interrupted':
            print("\nExiting monitor (user interrupt)")
            break
        else:
            if restart_count >= MAX_RESTARTS:
                print(f"\n[ERROR] Max restarts ({MAX_RESTARTS}) reached. Stopping.")
                break
            
            print(f"\n[INFO] Waiting 10 seconds before restart...")
            time.sleep(10)
    
    if restart_count >= MAX_RESTARTS:
        print(f"\n[ERROR] Reached max restart limit ({MAX_RESTARTS}).")
        print(f"Last progress saved at: {get_last_progress()}")

if __name__ == "__main__":
    main()




