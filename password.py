name=input()
count=[0,0,0]
for i in name:
    if i.isupper():
        count[0]+=+1
    if i.islower():
       count[1]+=1
    if i.isnumeric():
        count[2]+=1
#count.sort()
if count[0]==0:
    print("0")
else:
    print(count)
        