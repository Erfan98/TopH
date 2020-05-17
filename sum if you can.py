t=int(input())
for i in range(t):
    n=int(input())
    if n%2==0:
        s=int(-(n/2))
    else:
        s=int(-((n-1)/2-1))
    
    print(s)