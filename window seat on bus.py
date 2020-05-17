t=int(input())
for i in range(t):
    l,w,d=map(float,input().split())
    r=l*(w/2-d/2)
    print("Case {0}: {1:.2f}".format(i+1,r))