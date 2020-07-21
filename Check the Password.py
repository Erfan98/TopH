def password_gen(name):
    s=0
    arr=[]
    n=len(name)
    for i in name:
        arr.append(ord(i))
        
    for j in arr:
        n-=1
        s=s+(j*(131**n))
    
    return s%100000007

#driver code
  #new=s+'1'
   # arr=[]
   # arr.append(password_gen(s))
   # arr.append(password_gen(new))
    
t=int(input())
arr=[]
for i in range(t):
    
    s1,s2=map(str,input().split())
    
    if s1=="Register":
        for x in range(10):
            name=s2+str(x)
            arr.append(password_gen(name))
            arr.append(password_gen(s2))
    
    elif s1=="Login":
        if int(s2) in arr:
            print("1")
        else:print("0")

