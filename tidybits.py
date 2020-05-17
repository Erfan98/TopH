n=int(input())
s=bin(n).replace("0b","").replace("0","")
s=str(s)
print(int(s,2))