s=int(input())
c=[0,0,0,0,0,0,0,0,0,0]
for i in s:
	if i=="0":
		c[0]+=1
	elif i=="1":
		c[1]+=1
	elif i=="2":
		c[2]+=1
    elif i=="3":
		c[3]+=1
    elif i=="4":
		c[4]+=1
    elif i=="5":
		c[5]+=1
    elif i=="6":
		c[6]+=1
    elif i=="7":
		c[7]+=1
    elif i=="8":
	    c[8]+=1
    elif i=="9":
		c[9]+=1

c.sort()
print(c[0])