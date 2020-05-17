s=iter(input())
count = 0
for i in s:
    if i<=6:
        count=count+1
o=int(count)/6
b=int(count)%6

if count==0:
    print(b+ "BALLS")
else:
    print(o + "OVER" + b + "BALLS")
        