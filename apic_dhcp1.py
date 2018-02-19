import requests
import json
from pprint import pprint

with open('data/off_dhcpLease.json') as f:
    data = json.load(f)

print('\n==================================')
pprint(data)

print('\n==================================')
stuff = data['imdata']
for d in stuff:
    print('{0:20}: {1:20}'.format(d['dhcpLease']['attributes']['clientId'], d['dhcpLease']['attributes']['ip']))

print('\n==================================')
with open('data/off_dhcpPool.json') as g:
    g_data = json.load(g)

pprint(g_data)

print('\n==================================')
with open('data/off_opflexODev.json') as h:
    h_data = json.load(h)

pprint(h_data)

print('\n==================================')
with open('data/off_topSystem.json') as j:
    j_data = json.load(j)

pprint(j_data)
