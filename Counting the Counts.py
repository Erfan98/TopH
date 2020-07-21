bla=input()
count=0
l=list(map(int,input().split()))
for i in l:
    if i>=80:
        count+=1
    
print(count)