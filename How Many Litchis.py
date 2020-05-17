x,y=map(int,input().split())
b=y-x+1
s=0
for i in range(x,y+1):
    s=s+i
if x==0 and y==0:
    print()
else:
    print("{0} {1}".format(b,s))