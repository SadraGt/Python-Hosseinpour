from sys import getsizeof
L = [x*x for x in range (500000)]
print(getsizeof(L))     #4167352 b

G = (x*x for x in range (500000))
print(getsizeof(G))     #104 b
print (*G)
##Or
# for i in G :
#     print (i)
