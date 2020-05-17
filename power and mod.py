#https://toph.co/p/power-and-mod
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    e=a**b
    m=e%c
    print(m)