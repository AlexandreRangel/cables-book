#!/usr/bin/env python3
"""
Monitor scraper progress and commit/push when done
"""

import json
import os
import sys
import time
import subprocess
from datetime import datetime

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

PROGRESS_FILE = "../browser_scrape_progress.json"
TOTAL_OPS = 1340
CHECK_INTERVAL = 30  # seconds

def get_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('last_index', 0)
    return 0

def commit_and_push():
    """Commit and push changes"""
    print("\n" + "=" * 60)
    print("SCRAPING COMPLETE! Committing and pushing...")
    print("=" * 60)
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir("..")  # Go to project root
    
    # Stage all changes
    print("\nStaging changes...")
    subprocess.run(["git", "add", "-A"], check=True)
    
    # Commit
    commit_msg = f"Update ops with descriptions and editor links - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    print(f"Committing: {commit_msg}")
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    
    # Push
    print("Pushing to remote...")
    subprocess.run(["git", "push"], check=True)
    
    print("\n[DONE] Successfully committed and pushed!")
    print("=" * 60)

def main():
    print("=" * 60)
    print("SCRAPER MONITOR - Will commit/push when done")
    print("=" * 60)
    print(f"Checking every {CHECK_INTERVAL} seconds...")
    print()
    
    last_progress = 0
    stalled_count = 0
    
    while True:
        progress = get_progress()
        pct = (progress / TOTAL_OPS) * 100 if progress > 0 else 0
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Progress: {progress}/{TOTAL_OPS} ({pct:.1f}%)")
        
        if progress >= TOTAL_OPS:
            # Done!
            time.sleep(10)  # Wait a bit for final saves
            commit_and_push()
            break
        
        # Check if stalled
        if progress == last_progress and progress > 0:
            stalled_count += 1
            if stalled_count >= 5:
                print(f"  Warning: Progress stalled at {progress} for {stalled_count * CHECK_INTERVAL}s")
        else:
            stalled_count = 0
        
        last_progress = progress
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()

