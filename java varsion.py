#https://toph.co/p/version-checker

v1,v2=map(str,input().split())
for i in v1:
    v1=v1.replace(".",",")

for i in v2:
    v2=v2.replace(".",",")

    
if(v1>v2):
    for i in v1:
        v1=v1.replace(",",".")
    print(v1)
elif(v1<v2):
    for i in v2:
        v2=v2.replace(",",".")
    print(v2)
else:
    if len(v1)>len(v2):
        for i in v1:
            v1=v1.replace(",",".")
        
        print(v1)
    else:
        for i in v2:
            v2=v2.replace(",",".")
        
        print(v2)

