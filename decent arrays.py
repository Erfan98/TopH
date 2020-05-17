n=input()
l=list(map(int,input().split()))
if l==sorted(l):
    print("Yes")
else:
    print("No")