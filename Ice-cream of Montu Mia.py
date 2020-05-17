s=int(input())
a,b,c=map(int,input().split())
x=min(a,b,c)
y=s-x
if y>=10:
    print("Yes :-D")
else:
    print("No :-(")
