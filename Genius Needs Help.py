t=int(input())
for i in range(t):
    a,b=map(int, input().split())
    s=int(a+b)
    print("Case #{0}: {1:d}".format(i+1,s))