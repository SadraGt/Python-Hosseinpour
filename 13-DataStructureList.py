Number = [1, 2, 3, 4, 5]

# for i in Number:
#     print(i**2)

L1 = [1, 2, 3]
L2 = [4, 5]
L3 = L1 + L2  #We can sum Lists
# print (L3)

L4 = [0]*20 # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# print (L4)

Matrix = [  [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]  ]
# print(Matrix)

x = (list("Hello World"))
# print(x)
# print(len(x))

Number = [1, 2, 3, 4, 5]

Number[0] = 15  # change 0==1 to 0==15 
# print(Number)

# print(Number[:2])      # [15, 2]
# print(Number[1:3])     # [2, 3]
# print(Number[-2:])     # [4, 5]
# print(Number[:-2])     # [15, 2, 3]
# print(Number[::2])     # [15, 3, 5]
# print(Number[::-1])    # [5, 4, 3, 2, 15]  *Revers*
# print(Number[1])       # 2
# print(Number[-1])      # 5
# print(Number[:])       # [15, 2, 3, 4, 5]

Numbers = range(20)
# print(Numbers)  # range(0, 20)

# print(list(Numbers))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# print(list(Numbers))

Numbers = list(range(20))
# print(Numbers[::2])   # Even:   [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# print(Numbers[1::2])  # Odd :   [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# print(len(Numbers)) # 20

 
Letters = ['A', 'B', 'C', 'D']

# for letter in Letters:
    # print (letter)
# A
# B
# C
# D

# for index, letter in enumerate(Letters):
    # print(f"{letter} index is : {index} ")
# A index is : 0 
# B index is : 1 
# C index is : 2 
# D index is : 3

values = ['A' , 125, [2,5], ['c','f']]

Letters = ['A', 'B', 'C', 'D']
Letters.append('A')
Letters.append(['P', 'V'])
Letters.extend(['L' , 'B'])

print(Letters) # ['A', 'B', 'C', 'D', 'A', ['P', 'V'], 'L', 'B']

Letters.remove('B')
print(Letters) # ['A', 'C', 'D', 'A', ['P', 'V'], 'L', 'B']

Letters.pop(5)
print(Letters) # ['A', 'C', 'D', 'A', ['P', 'V'], 'B']

del Letters[1:3]
print(Letters) # ['A', 'A', ['P', 'V'], 'B']