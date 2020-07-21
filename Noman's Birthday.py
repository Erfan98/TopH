n=int(input())
l=input()
def chekDuplicate(n,l):
	for i in range(len(l)-1):
		if l[i]==l[i+1]:
			print("Change needed")
			return
	print("No change needed")
	
chekDuplicate(n,l)
