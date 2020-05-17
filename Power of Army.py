t=int(input())
for i in range(t):
    bla=input()
    l=list(map(int,input().split()))
    M=sorted(l,reverse=True)
    print(M[0]-M[-1])
    