from array import array

A = array('i', [1, -2, 3, 4])
print(A)

A.append(85)
print(A)

A.remove(-2)
print(A)

A.insert(2,2000)
print(A)

Ltest = [1, 3, 2000, 4, 85]
A = array('i', Ltest)