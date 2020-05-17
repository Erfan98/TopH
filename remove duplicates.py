def count_dict(mystring):
    d = {}
# count occurances of character
    for w in mystring: 
        d[w] = mystring.count(w)
       # print(d)
# print the result
    for k in d:
        print (k + ' ' + str(d[k]))

t=int(input())
for i in range(t):
    mystring=input()
    print("Case #{}:".format(i+1))
    count_dict(mystring)