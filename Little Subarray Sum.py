bla,a,b=map(int,input().split())
l=list(map(int,input().split()))
nl=l[a:b+1]
s=0
for i in nl:
    s=s+i

print(s)