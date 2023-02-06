Type1 = [3, 6]
Type2 = (3, 6)

print(type(Type1))  # <class 'list'>
print(Type1)        # [3, 6]

print(type(Type2))  # <class 'tuple'>
print(Type2)        # (3, 6)

Type1[0] = 9
#- Type2[0] = 9    # can not Because tuple is immutable

Type2 = 3, 6
print(Type2)  # (3, 6)

Type2 = tuple([3, 6])
print(Type2)  # (3, 6)

Type2 = tuple("Sadra")
print(Type2)  # ('S', 'a', 'd', 'r', 'a')

t = ("A", "B", "C", "D")
f, m, *_ = t

for i in t :
    print(i)