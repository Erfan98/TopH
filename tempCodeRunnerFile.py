
def gpacalc(marks,credit):
    gpc=0
    if marks>=80 and marks<=100:
        gp=4.00
        gpc=float(gpc)
        gpc=gp*credit
        return gpc

    if marks>=75 and marks<80:
        gp=3.75
        gpc=float(gpc)
        gpc=gp*credit
        return gpc
    
    if marks>=70 and marks<75:
        gp=3.50
        gpc=float(gpc)
        gpc=gp*credit
        return gpc

    if marks>=65 and marks<70:
        gp=3.25
        gpc=float(gpc)
        gpc=gp*credit
        return gpc

    if marks>=60 and marks<65:
        gp=3.00
        gpc=float(gpc)
        gpc=gp*credit
        return gpc

    if marks>=55 and marks<60:
        gp=2.75
        gpc=float(gpc)
        gpc=gp*credit
        return gpc


    if marks>=50 and marks<55:
        gp=2.50
        gpc=float(gpc)
        gpc=gp*credit
        return gpc
    
    if marks>=45 and marks<55:
        gp=2.25
        gpc=float(gpc)
        gpc=gp*credit
        return gpc

    if marks>=40 and marks<45:
        gp=2.00
        gpc=float(gpc)
        gpc=gp*credit
        return gpc




t=int(input())

for i in range(t):
    total_credit=0
    count=0
    sumation=0
    gpc=0
    course=int(input())
    for j in range(1,course+1):
        marks,credit=map(float,input().split())
        total_credit+=credit
        if marks>=40 and marks<=100:
            sumation=(sumation+gpacalc(marks,credit))
            
            gpa=sumation/total_credit
        
        else:
            count+=1

    if count==0:
        print("Case {0}: {1:.2f}".format(i+1,gpa))
    elif count==1:
        print("Case {}: Sorry, you have failed in 1 course!".format(i+1))
    else:
        print("Case {0}: Sorry, you have failed in {1} courses!".format(i+1,count))

