s=input()
upper=0
lower=0
for i in s:
    if i.isupper():
        upper+=1

    
    if i.islower():
        lower+=1

print("{0} {1}".format(upper,lower))

    