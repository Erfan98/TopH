t=int(input())
for i in range(t):
    n=int(input())
    s="Harry! Khelbe Hogwarts, Jitbe Hogwarts!"
    S=s.replace("y","y"*n)
    print("Case {0}:{1}".format(i+1,S))