#!/usr/bin/env python3
"""
Continuous scraper runner - restarts scraper if it fails
Simple version that just runs the scraper and restarts on failure
"""

import subprocess
import time
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRAPER_SCRIPT = os.path.join(SCRIPT_DIR, "browser_op_scraper.py")
MAX_RESTARTS = 50

def main():
    restart_count = 0
    
    print("="*60)
    print("Continuous Scraper Runner")
    print("="*60)
    print("Will restart scraper automatically if it crashes")
    print(f"Max restarts: {MAX_RESTARTS}")
    print("="*60)
    print()
    
    while restart_count < MAX_RESTARTS:
        print(f"\n[{restart_count}] Starting scraper...")
        print("-" * 60)
        
        # Run the scraper directly (output goes to console)
        result = subprocess.run(
            [sys.executable, SCRAPER_SCRIPT, '--resume'],
            cwd=SCRIPT_DIR
        )
        
        if result.returncode == 0:
            print("\n" + "="*60)
            print("SUCCESS! Scraper completed.")
            print("="*60)
            break
        else:
            restart_count += 1
            print(f"\n[ERROR] Scraper exited with code {result.returncode}")
            
            if restart_count < MAX_RESTARTS:
                print(f"[INFO] Restarting in 5 seconds... (restart #{restart_count}/{MAX_RESTARTS})")
                time.sleep(5)
            else:
                print(f"[ERROR] Max restarts reached ({MAX_RESTARTS})")
                break
    
    print("\nMonitor stopped.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Stopping monitor.")
        sys.exit(0)

