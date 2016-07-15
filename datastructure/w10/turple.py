name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
for line in handle:
    if line.startswith('From '):
        hour = line.split(' ')[6].split(':')[0]
        dic[hour] = dic.get(hour,0)+1
        
for k,v in sorted(dic.items()):
    print str(k)+' '+str(v)