import math
t=int(input())

for i in range(t):
    count=0
    bla=input()
    l=list(map(int,input().split()))
    for j in l:
        x=math.floor(math.sqrt(j))
        if pow(x,2)==j:
            count+=1

    if len(l)==count:
        print("YES")
    else:print("NO")

