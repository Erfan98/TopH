x,y=map(int, input().split())
def computeGCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 


lcm=int(x*y/computeGCD(x,y)
if computeGCD(x,y)+lcm==x+y:
    print("true")