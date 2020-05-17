#https://toph.co/p/an-arithmetic-problem
t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    if l[2]-l[1]==l[1]-l[0]:
        nth=l[0]+(l[3]-1)*(l[1]-l[0])
        print("Case {0}: {1}".format(i+1,nth))
    else:
        print("Case {0}: Error".format(i+1))
