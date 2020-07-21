t=int(input())
for i in range(t):
    n1,n2=map(str,input().split())
    if n1[0:3]==n2[0:3]:
        print("YES")
    else:
        print("NO")
        