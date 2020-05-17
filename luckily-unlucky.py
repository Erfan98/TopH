#https://toph.co/p/luckily-unlucky
bla=input()
count=0
l=list(map(int,input().split()))
for i in l:
    if i%7==0:
        count+=1
    
if count==13:
    print("Luckily Unlucky")
else:
    print("Lucky")