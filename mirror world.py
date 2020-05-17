t=int(input())
for i in range(t):
    x,y=map(str, input().split())
    xr=int(x[::-1])
    yr=int(y[::-1])

    if xr<yr: print("{0} < {1}".format(x,y))
    elif xr>yr: print("{0} > {1}".format(x,y))
    elif xr==yr: print("{0} = {1}".format(x,y))