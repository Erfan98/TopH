n=input()
s=list(map(int,input().split()))
count=0
for i in s:
    if i%3==0:
        count+=1

print(count)