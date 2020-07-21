from math import *

def checkValidity(a, b, c):  
      
    # check condition  
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True 


t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if checkValidity(a,b,c):
        s=(a+b+c)/2
        area=sqrt(s*(s-a)*(s-b)*(s-c))
        print("{:.2f}".format(area))
    else:
        print("Oh, No!")