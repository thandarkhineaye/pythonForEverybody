import urllib.request as ur
import json


jsonURL = input('Enter location: ')
if len(jsonURL) < 1:
    quit()

parms = dict()
parms['address'] = jsonURL

print('Retrieving', jsonURL)

data = ur.urlopen(jsonURL).read().decode('utf-8')
print('Retrieved', len(data), 'characters')

info = json.loads(data)

print('Retrieved', len(info), "characters")
numCount = 0
total = 0
   
for item in info['comments']:
    numCount = numCount + 1
    total = total + int(item['count'])
print('Count:', numCount)
print('Sum:', total)
