sm="abcdefghijklmnopqrstuvwxyz"
up=sm.upper()
num="1234567890"
while True:
	try:
		s=input()
		isu=False
		iss=False
		isn=False
		c=0
		for i in s:
			if not sm.find(i)==-1:
				iss=True
			elif not up.find(i)==-1:
				isu=True
			elif not num.find(i)==-1:
				isn=True
			if iss and isu and isn:
				iss=False
				isu=False
				isn=False
				c+=1
		print(c)
		
	except:
		break