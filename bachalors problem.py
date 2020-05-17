t=int(input())
for i in range(t):
    m1=list(map(int,input().split()))
    b=int(input())
    m2=list(map(int,input().split()))
    b2=sum(m2)-(b-sum(m1))
    if b2>=0: print("Case {0}: {1}".format(i+1,b2))
    else: print("Case {0}: 0 ".format(i+1))