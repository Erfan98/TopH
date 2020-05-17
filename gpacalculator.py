t= int(input())
sumation=0
for i in range(t):
    sub=[]
    s=int(input())
    for j in range (s):
       ts=float(input()) 
       sub.append(ts)


    sumation=sum(sub)
    gpa=float(sumation/s)
    print("Case {0}: {1:.3f}".format(i+1,gpa))
    sumation=0