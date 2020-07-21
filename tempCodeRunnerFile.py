arr=[]
t= int(input())
for i in range(t):
    string=input()
    if string in arr:
        if string[-1].isnumeric()==False:
            print(string+'1')
        else:
            num=int(string[-1])+1
            string.replace(string[-1],'num')
            print(string)
            
        
        
    else:
        print("OK")
    arr.append(string)

    