import re
x = open('data2.txt','r').read()

y = re.findall('[0-9]+', x)
sum = 0;
for num in y:
	sum += int(num)
print sum