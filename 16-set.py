L1 = ['A', 'B', 'C', 'V', 'B']
S1 = set(L1)
S2 = {'A' , 'T', 'C', 'G', 'I'}
S3 = set([5, 9, 5])

# print(S1)   # {'B', 'A', 'C', 'V'}  B^2 --> B^1 
# print(S2)   # {'G', 'C', 'T', 'A', 'I'}
# print(S3, end="\n\n")   # {9, 5}


S3.add('A')
S3.add('A')
# print(S3)

S3.remove('A')
# print(S3)

## print(S3[1]) and ... is not work 





# Union S1 and S2
MyUnion = S1 ^ S2
MyUnion = S1.union(S2)
MyUnion = set.union(S1 ,S2)

# print (MyUnion, end="\n\n")


# Intersection S1 and S2
MyIn = S1 & S2 
MyIn = S1.intersection(S2)
MyIn = set.intersection(S1, S2)

# print(MyIn, end="\n\n")

# S1 - S2
MyM = S1 - S2

# print(MyM, end="\n\n")

# Symmetric difference /// Union(S1,S2) - Intersection(S1,S2) 
MySD = S1 ^ S2
# print(MySD)