#!/usr/bin/env python3
import requests
import re
import json

BASE_URL = 'https://cables.gl'

# Get main ops page
print("Getting main ops page...")
response = requests.get(f'{BASE_URL}/ops/', timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
print(f'Got main page: {len(response.text)} bytes')

# Find namespace links
namespace_pattern = r'href="/ops/(Ops\.[A-Za-z0-9.]+)"'
namespaces = list(set(re.findall(namespace_pattern, response.text)))
print(f'Found {len(namespaces)} namespaces:')
for ns in sorted(namespaces):
    print(f'  {ns}')

# Find all op links directly
op_pattern = r'href="/op/(Ops\.[A-Za-z0-9_.]+)"'
all_ops = list(set(re.findall(op_pattern, response.text)))
print(f'\nFound {len(all_ops)} ops on main page')
print("Sample ops:")
for op in sorted(all_ops)[:20]:
    print(f'  {op}')

# Save to file
with open('test_ops_list.json', 'w') as f:
    json.dump({'namespaces': sorted(namespaces), 'ops': sorted(all_ops)}, f, indent=2)
print('\nSaved to test_ops_list.json')

