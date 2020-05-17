def validmove(x1,x2,y1,y2):
    if (x2-x1 ==y2-y1):
        return print("Yes")

    elif(-x2 + x1 ==y2 -y1):
        return print("Yes")

    else:
        return print("No")

t=int(input())
for i in range(t):
    x1,y1,x2,y2=map(int,input().split())
    validmove(x1,x2,y1,y2)