def nCr(n, r): 
  
    return (fact(n) / (fact(r)  
                * fact(n - r))) 
  
# Returns factorial of n 
def fact(n): 
  
    res = 1
      
    for i in range(2, n+1): 
        res = res * i 
          
    return res 
  
# Driver code 
t=int(input())
for i in range(t):
    n=int(input())
    result=int(nCr(n, 4))
    print("Case {0}: {1}".format(i+1,result)) 