import math
t= int(input())
for i in range(t):
    x,y=map(int,input().split())
    lcm=float((x*y)/math.gcd(x,y))
    if int(x*y)==int(lcm):
        print("yes")
    else:
        print("no")
