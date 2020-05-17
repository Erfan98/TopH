#https://toph.co/p/arya-and-or

t=int(input())
result=0
for i in range(t):
    n=input()
    l=list(map(int,input().split()))
    for j in l:
       result=result|j
    
    print("Case {0}: {1}".format(i+1,result))