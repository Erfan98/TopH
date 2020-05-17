a11,a12=map(int,input().split())
a21,a22=map(int,input().split())

b11,b12=map(int,input().split())
b21,b22=map(int,input().split())

c11=(a11*b11)+(a12*b21)
c12=(a11*b12)+(a12*b22)
c21=(a21*b11)+(a22*b21)
c22=(a21*b12)+(a22*b22)

print("{0} {1}".format(c11,c12))
print("{0} {1}".format(c21,c22))