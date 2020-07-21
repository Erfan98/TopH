n=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(len(l)):
	sum+=l[i]
	print(float(sum/(i+1)))