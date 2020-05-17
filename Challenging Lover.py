def prime_test(N):
    count=0
    for i in range(1,N+1):
        if N%i==0:
            count+=1
    
    if count==2:
        print("Yes")
    else:print("No")



t=int(input())
d=[]
for i in range(t):
    n=int(input())
    for j in range(1,n+1):
        if n%j==0:
            d.append(j)
    
    N=sum(d)
    d=[]
    prime_test(N)