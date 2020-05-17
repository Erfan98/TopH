#https://toph.co/p/byangs-day-out
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if (a+b>=c and a+c>=b and b+c>=a):
            print ("Yes")
    else:
        print ("No")