while True:
    try:
        n,m=map(int,input().split())
        s=0
        for i in range(n,m+1):
            s=s+i

        print("Sum of {0} to {1} is -> {2};".format(n,m,s))
        
    except EOFError:
        break