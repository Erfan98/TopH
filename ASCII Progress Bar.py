import math
n=float(input())
n1=math.floor(n)
n2=n1//10
print("[", end = '')
for i in range(10):

    if i<n2:
        print("+", end = '')
    
    else:
        print(".", end = '')

print("] {0}%".format(n1))