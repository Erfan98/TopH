#import math
#t= int(input())
#for i in range(t):
 #   a,b=map(int, input().split())
  #  lcm=(a*b)/math.gcd(a,b)
   # if math.gcd(a,b)+lcm==a+b:
    #    print("true")
    #else:
     #   print("false")

def computeGCD(x, y): 

     while(y): 
       x, y = y, x % y 
  
    return x
a,b=map(int, input().split())
a = 60
b= 48
  
print (computeGCD(60,48)) 