t=int(input())
s=0
for i in range(t):
    s=0
    a,b=map(int,input().split())
    for j in range(a,b):
        if j%2!=0:
            s=s+j
        
    
    stdout.write("Case {0}: {1}".format(i+1,s))