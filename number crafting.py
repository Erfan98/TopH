t=int(input())
for i in range(t):
    n=input()
    s=list(map(int,input().split()))
    if min(s)==0:
        print("NULL")
        break
    else:
        r=sum(s)//min(s)

    index=[]
    for j in range(len(s)):
        if s[j]==r:
            index.append(j)
    
    index1=[x+1 for x in index]
    if len(index1)>0:
        print(*index1)
    else:
        print("NULL")
