import itertools
def remove_consecutive_duplicates(s1):
     return (''.join(i for i, _ in itertools.groupby(s1)))
 
 #driver code
t=int(input())
for i in range(t):
    print(remove_consecutive_duplicates(input()))