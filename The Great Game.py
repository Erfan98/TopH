t=int(input())
for i in range(t):
    num=int(input())
    ar=[int(x) for x in str(num)]
    if len(str(num))%2==0 and sum(ar)%2==0:
        print("Case {}: Safe to push".format(i+1))
    elif len(str(num))%2!=0 and sum(ar)%2!=0:
        print("Case {}: Safe to push".format(i+1))
    else:
        print("Case {}: BOOM".format(i+1))