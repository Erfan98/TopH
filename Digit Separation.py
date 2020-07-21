while True:
    try:
        s=0
        n=input()
        for i in n:
            s+=int(i)
            
        print(s)
        
        #Another Approch
        # n=input()
        # l=[int(i) for i in n]
        # print(sum(l))

    except EOFError:
        break
    
#Another Approch
n=input()
l=[int(i) for i in n]
print(sum(l))

