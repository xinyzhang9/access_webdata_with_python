import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
sum = 0;
spans = soup('span')
for span in spans:
   	sum += int(span.text)

print sum
