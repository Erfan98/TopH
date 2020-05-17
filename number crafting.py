t=int(input())
for i in range(t):
    n=input()
    s=list(map(int,input().split()))
    r=round(sum(s)/min(s))
    for i in s:
        if i==r:
            print(s.index(r)+1)
            break
        else:
            print("NULL")
