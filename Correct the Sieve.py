t=int(input())
for i  in range(t):
    n=int(input())
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
        
    if(count==2):print("{0} is a prime number.".format(n))
    else:print("{} is not a prime number.".format(n))