t=int(input())
for i in range(t):
    l=list(map(str,input().split()))
    if l[0]==l[2]:print("Possible")
    elif l[0]==l[3]:print("Possible")
    elif l[1]==l[2]:print("Possible")
    elif l[1]==l[3]:print("Possible")
    else:print("Oh no!, such a shame")
