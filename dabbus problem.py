import math
t=int(input())
for i in range(10):
    d,a=map(int,input().split())
    x=d/math.tan(a*(math.pi)/360)
    print(x)