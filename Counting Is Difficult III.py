from math import factorial
def nCr(n, r): 
  
    return (factorial(n) / (factorial(r) * factorial(n - r)))

#driver code
t=int(input())
for i in range(t):
    s,j=map(int,input().split())
    result=int(nCr(s,3)+nCr(j,3))
    print("Case {}: {}".format(i+1,result))
