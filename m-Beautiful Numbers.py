def beautiful_number(start,final,n):
    for i in range(start,final+1):
        count=0
        s=sum([int(j) for j in str(i)])
        if i%n==0 and s%n==0:
            count+=1
    
    return count

#driver code
start,final,n=map(int,input().split())
print(beautiful_number(start,final,n))
    