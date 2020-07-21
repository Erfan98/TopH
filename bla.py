t=int(input())
for i in range(t):
	n=int(input())
	s=0
	l=list(map(int,input().split()))
	for j in range(len(l)):
		if j!=len(l)-1:
			if l[j]%2==0:
				s+=l[j]//2
			elif l[j]<2:
				s+=0
			else:
				if l[j+1]%2!=0:
					l[j+1]-=1
					s+=(l[j]//2)+1
				else:
					s+=(l[j]//2)
		else:
			if l[j]<2:
				s+0
			else:
				s+=l[j]//2
	print(s)