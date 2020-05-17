while True:
    a,b,c=map(int,input().split())
    if a==b==c==0:
        quit()
    else:
        r=pow(a,b)%c
        print(r)
