l=list(map(int,input().split()))
b=int(input())
l1=sorted(l)
t=b-l1[0]
average=t/(len(l1)-1)
print("%.2f" %average)
