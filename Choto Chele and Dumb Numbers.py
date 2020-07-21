def isPrime(n):
    c=0
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                c+=1
            else:
                c+=0
        if c==0:
            return True
        else:
            return False

def add()  
#driver code
t=int(input())
for i in range(t):
    count=0
    n,m=map(int,input().split())
    for j in range(n,m+1):
        if isPrime(j)==True:
            count+=1
    print("Case {}: {}".format(i+1,count))
    
                
