n,m=map(int,input().split())
N=n*m
s=""
string=str(N)
L="1"*len(str(N))
for i in string:
    s=s+str((int(i)+1))

print(s)
