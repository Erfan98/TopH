a,b,c=map(int,input().split())
if b<=a and c<=a:
    print("Chocolate")
elif b>=a and c>=a:
    print("Chocolate")
else:
    if b<=a and c>=a:
        print("Chocolate")
    elif b>=a and c<=a:
        print("Ice-cream")

