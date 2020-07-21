while True:
    try:
        n,m=map(int,input().split())
        if n>m:
            n,m=m,n
        
        s=0
        s=sum(range(n,m+1))

        print("Sum of {0} to {1} is -> {2};".format(n,m,s))
        
    except EOFError:
        break