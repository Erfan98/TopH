t=int(input())
for i in range(t):
    s=input()
    S=list(s)
    for j in range(0,len(S)+1):
        if S[j]==S[j+1]:
            S[j+1]="#"
        
    print(S)