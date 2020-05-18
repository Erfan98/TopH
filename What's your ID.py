def sub(s):
    if s[4:7]=="115":
        sub="CSE"
        return sub
    
    elif s[4:7]=='141':
        sub="EEE"
        return sub
    
    elif s[4:7]=='116':
        sub="BBA"
        return sub

    elif s[4:7]=='117':
        sub="LLB"
        return sub

    elif s[4:7]=='114':
        sub="English"
        return sub

    elif s[4:7]=='111':
        sub="Economics"
        return sub

def term(s):
    if s[2:3]=="1":
        t="Spring"
        return t
    if s[2:3]=="2":
        t="Summer"
        return t
    if s[2:3]=="3":
        t="Autumn"
        return t


t=int(input())
for i in range(t):
    s=input()
    year=s[0:2]
    print("{0} {1} 20{2}".format(sub(s),term(s),year))


