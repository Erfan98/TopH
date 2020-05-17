t=int(input())
for i in range(t):
    d=int(input())
    print("Case {}:".format(i+1))
    total=1
    for i in range(d):
        if i==0:
            new=0
            total+=new
            print("Day = {0}, New = {1}, Total = {2}".format(i+1,new,total))


        else:
            new=total*2
            total+=new
            print("Day = {0}, New = {1}, Total = {2}".format(i+1,new,total))