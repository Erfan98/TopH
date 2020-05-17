import datetime
t=int(input())
for i in range(t):
    d,m,y=map(int,input().split())
    x = datetime.datetime(y,m,d) + datetime.timedelta(days=1)

    print(x.strftime("%d %b, %Y"),) 