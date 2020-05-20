def cal(n):
    if (n==1):
        return 1
    
    elif(n%2==0):
        x=cal(n)
        return x**2+1
    
    else:
        x=cal(n)*cal(n+1)
        return x+2
	

n=int(input())
print(cal(n))
