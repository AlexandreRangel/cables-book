#!/usr/bin/env python3
"""Monitor scraper progress in real-time"""

import json
import os
import time
import sys
from datetime import datetime

PROGRESS_FILE = "../browser_scrape_progress.json"
DATA_FILE = "../browser_ops_data.json"

def get_progress():
    """Get current progress from files"""
    progress = {
        'last_index': 0,
        'total_ops': 0,
        'namespaces': {},
        'last_updated': None
    }
    
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            progress['last_index'] = data.get('last_index', 0)
            progress['last_updated'] = data.get('last_updated', '')
            if 'ops' in data:
                total = 0
                for ns, ops in data['ops'].items():
                    count = len(ops)
                    total += count
                    progress['namespaces'][ns] = count
                progress['total_ops'] = total
    
    return progress

def main():
    print("=" * 60)
    print("SCRAPER PROGRESS MONITOR")
    print("=" * 60)
    print()
    
    last_index = 0
    iteration = 0
    
    try:
        while True:
            progress = get_progress()
            current = progress['last_index']
            
            if current > last_index:
                # Progress update
                pct = (current / 1340) * 100 if current > 0 else 0
                elapsed_ops = current - last_index
                rate = elapsed_ops / 5.0 if elapsed_ops > 0 else 0  # ops per 5 seconds
                remaining = (1340 - current) / rate if rate > 0 else 0
                
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Progress: {current}/1340 ({pct:.1f}%)")
                print(f"  Processed: {elapsed_ops} ops in last 5 seconds ({rate:.1f} ops/sec)")
                print(f"  Estimated time remaining: {remaining/60:.1f} minutes")
                print(f"  Last updated: {progress.get('last_updated', 'unknown')}")
                
                # Show namespace breakdown
                if progress['namespaces']:
                    recent_ns = sorted(progress['namespaces'].items(), key=lambda x: x[1])[-5:]
                    print(f"  Top namespaces: {dict(recent_ns)}")
                
                print()
                last_index = current
            elif iteration == 0:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Waiting for scraper to start...")
                print(f"  Current progress: {current}/1340")
                if progress.get('last_updated'):
                    print(f"  Last updated: {progress['last_updated']}")
                print()
            
            iteration += 1
            time.sleep(5)  # Check every 5 seconds
            
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped.")
        final = get_progress()
        print(f"\nFinal progress: {final['last_index']}/1340")

if __name__ == "__main__":
    main()

