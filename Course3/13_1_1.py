import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

xmlURL = input('Enter location: ')
if len(xmlURL) < 1:
    quit()

parms = dict()
parms['address'] = xmlURL

print('Retrieving', xmlURL)
uh = urllib.request.urlopen(xmlURL, context=ctx)

data = uh.read()
tree = ET.fromstring(data)

count = tree.findall('.//count')
numCount = 0
total = list()
countlen = len(count)
for i in range(countlen):
    numCount = numCount + 1
    total.append(int(count[i].text))


print("Count:", numCount)
print("Sum:", sum(total))
#total = total + int(count[0].text)