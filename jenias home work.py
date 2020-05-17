import math
t=int(input())

for i in range(t):
    a1=float(input())
    a2=float(a1-(math.pi*(math.sqrt(a1)/2)**2))
    print(a2)
    print(math.pi*math.sqrt(a1))



