import math
t=int(input())
for i in range(t):
    n=int(input())
    rt=float(math.sqrt(n))

    if rt%math.floor(rt)!=0:
        print("NO.")

        
    else:
        if rt<2:
            print("NO.")
        elif rt==2:
            print("YES.")
        else:
            r=int(rt)
            for j in range(2,r):
                if (r%j)==0:
                    print("YES.")
                    break
                else:
                    print("NO.")
                    break