a,b=map(int,input().split())
c,d=map(int,input().split())

x=max(a*b,a*c,a*d,b*c,b*d,c*d)
print(x)
