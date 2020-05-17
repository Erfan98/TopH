t=int(input())
for i in range(t):
    s=input()
    m= int((len(s) - 1)/2)
    ns=s[0:m]
    print(ns[::-1])