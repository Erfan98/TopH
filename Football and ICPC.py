bla=int(input())
S=[]
A=list(map(int,input().split()))
B=list(map(int,input().split()))
for i in range(bla):
    S.append((A[i]*20-B[i]*10))
if max(S)<0:
    print(0)
else:
    print(max(S))

