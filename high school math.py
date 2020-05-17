x,m,n=map(int,input().split())
b=int((n/(m+n))*x)
a=int(x-b)
print("{0} {1}".format(a,b))