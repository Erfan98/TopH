def isPrime(number):
    c=0
    if number==1:
        return False
    elif number==2:
        return True
    else:
        for k in range(2,number):
            if number%k==0:
                c+=1
            else:
                c+=0
        
        if c==0:
            return True
        else:
            return False
        
def primeList(inital,terminator):
    prime_list=[]
    for j in range(inital,terminator+1):
        if isPrime(j)==True:
            prime_list.append(j)
        
    if len(prime_list)==0:
        return -1
    else:
        prime_list.sort(reverse=True)
        return prime_list[0]
    


#drive_code
t=int(input())
for i in range(t):
    p,q=map(int,input().split())
    print(primeList(p,q))
    

                