t=int(input())
for i in range(t):
    r=float(input())
    ra=float(8*pow(r,2))
    ca=float(2*3.1416*pow(r,2))
    s=ra-ca
    print("Case {0}:".format(i+1),"%.2f" %s)