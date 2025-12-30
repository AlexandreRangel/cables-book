#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime

# Fix encoding for Windows
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

PROGRESS_FILE = "../browser_scrape_progress.json"

print('=' * 60)
print('SCRAPER PROGRESS CHECK')
print('=' * 60)
print()

if os.path.exists(PROGRESS_FILE):
    with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
        d = json.load(f)
    idx = d.get('last_index', 0)
    pct = idx/1340*100 if idx > 0 else 0
    last_updated = d.get('last_updated', 'unknown')
    
    print(f'[OK] Progress File Found')
    print(f'  Current: {idx}/1340 ops ({pct:.1f}%)')
    print(f'  Last updated: {last_updated}')
    
    ops = d.get('ops', {})
    total_saved = sum(len(v) for v in ops.values())
    print(f'  Namespaces processed: {len(ops)}')
    print(f'  Total ops saved: {total_saved}')
    
    # Calculate rate
    if idx > 0:
        try:
            last_time = datetime.fromisoformat(last_updated.replace('Z', '+00:00'))
            now = datetime.now(last_time.tzinfo if last_time.tzinfo else None)
            if last_time.tzinfo:
                elapsed = (now - last_time).total_seconds()
            else:
                elapsed = (datetime.now() - last_time).total_seconds()
            
            if elapsed < 300:  # Less than 5 minutes
                rate = idx / max(elapsed, 1)
                remaining = (1340 - idx) / rate if rate > 0 else 0
                print(f'  Processing rate: {rate:.2f} ops/sec')
                print(f'  Estimated time remaining: {remaining/60:.1f} minutes')
        except:
            pass
    
    # Show recent namespaces
    if ops:
        recent = sorted(ops.items(), key=lambda x: len(x[1]), reverse=True)[:5]
        print(f'\n  Top namespaces processed:')
        for ns, op_list in recent:
            print(f'    {ns}: {len(op_list)} ops')
    
    # Check if scraper might be stuck
    if idx > 0:
        status = "[ACTIVE]" if idx < 1340 else "[COMPLETE]"
        print(f'\n  Status: {status}')
else:
    print('[INFO] Progress file not found')
    print('  Possible reasons:')
    print('    - Scraper is still initializing (fetching ops list)')
    print('    - Scraper has not started yet')
    print('    - Scraper is saving first 2 ops...')
    print('\n  Wait 1-2 minutes and check again')

print()
print('=' * 60)

