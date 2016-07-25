res = 1
for i in range(253):
	res *= 364/365.0

# print res

cnt = 365.0
for i in range(1,24):
	
	res *= (cnt-1)/cnt
	cnt -= 1.0

print res