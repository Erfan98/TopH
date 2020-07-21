s=input()
#UUDDLRLRBA
l=[0,0,0,0,0,0]
for i in s:
    if i=="U":
        l[0]+=0.5

    if i=="D":
        l[1]+=0.5

    if i=="R":
        l[2]+=0.5
    
    if i=="L":
        l[3]+=0.5

    if i=="B":
        l[4]+=1

    if i=="A":
        l[5]+=1


print(l)