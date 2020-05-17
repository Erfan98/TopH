bla,bla2=map(int,input().split())
s1=set(map(int,input().split()))
s2=set(map(int,input().split()))
s3=list(sorted((s1.union(s2))))

for i in s3:
    if s3[-1]==i: print("{0}".format(i),end="")
    else: print("{0} ".format(i),end="")