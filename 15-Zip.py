List1 = [1, 2, 3]
List2 = ['A', 'B', 'C']
#List3 = [(1, 'A'), (2, 'B'), (3, 'C')]

List3 = zip(List1, List2)
print(List3) # <zip object at 0x000001EF6EF33640>

List3 = list(zip(List1, List2))
print(List3) # [(1, 'A'), (2, 'B'), (3, 'C')]

List3 = list(zip(List1, [8, 9, 10], List2))
print(List3) # [(1, 8, 'A'), (2, 9, 'B'), (3, 10, 'C')]

List3 = list(zip(List1, [8, 9], List2))
print(List3) # [(1, 8, 'A'), (2, 9, 'B')]