#https://toph.co/p/aryas-counting
T=int(input())
for i in range(0, T):
    a, b, c=map(int, input().split())
    if a==b or b==c or a==c:
        r="Confused"
    r=max(a,b,c)
    
        
    print("Case",str(i+1)+":",r)
        
    