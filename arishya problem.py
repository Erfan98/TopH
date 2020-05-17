import math
t= int(input())
for i in range(t):
    r,a=map(float,input().split())
    area=float((a/360)*math.pi*pow(r,2))
    print(area)