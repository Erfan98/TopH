t=int(input())
s=0
l=0
for i in range(t):
    n,m=map(str,input().split())
    for i in range(n,m+1):
        s=s+sum(int(j) for j in str(i))
    
    for k in range(n,m+1):
        l=l+sum(int(o) for o in str(len(str(k))))
        
    print(l,s)
        