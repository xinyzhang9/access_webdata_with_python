import json
import urllib

url = raw_input("input url: ")
response = urllib.urlopen(url)
data = json.loads(response.read())

sum = 0
for item in data['comments']:
    sum += item['count']

print sum
