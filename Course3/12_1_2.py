from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
num = 0
# Retrieve all of the anchor tags
tags = soup("span")

for tag in tags:
    # Look at the parts of a tag
    count = count + 1
    a = int(tag.contents[0])

    num = num + a
print("Count", count)
print("Sum", num)