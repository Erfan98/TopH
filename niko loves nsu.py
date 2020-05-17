n=int(input())
s=input()
c=[0,0,0]
for i in s:
	if i=="N":
		c[0]+=1
	elif i=="S":
		c[1]+=1
	elif i=="U":
		c[2]+=1
c.sort()
print(c[0])