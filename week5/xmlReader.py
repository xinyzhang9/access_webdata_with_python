import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_'

while True:
    address = raw_input('Enter number: ')
    if len(address) < 1 : break

    url = serviceurl + address + '.xml'
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')
    sum = 0
    for count in counts:
        sum += int(count.text)

    print sum