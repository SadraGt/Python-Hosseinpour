Number = [2, 8, 12, 5, 19, 45, 1, 7, 10 ,4]

Number.sort()
# print(Number)                    # [1, 2, 4, 5, 7, 8, 10, 12, 19, 45]

Number.sort(reverse=True)
# print(Number)                    # [45, 19, 12, 10, 8, 7, 5, 4, 2, 1]

# print(Number)                    # [45, 19, 12, 10, 8, 7, 5, 4, 2, 1]

Number = [2, 8, 12, 5, 19, 45, 1, 7, 10 ,4]

# x = sorted(Number)
# print(x)                         # [1, 2, 4, 5, 7, 8, 10, 12, 19, 45]

# x = sorted(Number, reverse=True)
# print(x)                         # [45, 19, 12, 10, 8, 7, 5, 4, 2, 1]

# print(Number)                    # [2, 8, 12, 5, 19, 45, 1, 7, 10, 4]

Students = [("Ali", 17.5), ("Mariam", 18.5), ("Reza", 15.5), ("Fatime", 19.5), ("Sogol", 11.5),]
#              0     1          0       1        0     1         0        1        0       1 
def Sort_Key_Value(item):
    return item[1]

# x = sorted(Students,key=Sort_Key_Value, reverse=True)
# print(x)                                              # [('Fatime', 19.5), ('Mariam', 18.5), ('Ali', 17.5), ('Reza', 15.5), ('Sogol', 11.5)]
# print(Students)                                       # [('Ali', 17.5), ('Mariam', 18.5), ('Reza', 15.5), ('Fatime', 19.5), ('Sogol', 11.5)]

# Students.sort(key=Sort_Key_Value,reverse=True)
# print(Students) # [('Fatime', 19.5), ('Mariam', 18.5), ('Ali', 17.5), ('Reza', 15.5), ('Sogol', 11.5)]

Students.sort(key=lambda item: item[1], reverse=True)   # 9,8....,2,1
# print(Students)                                       # [('Fatime', 19.5), ('Mariam', 18.5), ('Ali', 17.5), ('Reza', 15.5), ('Sogol', 11.5)]
Students.sort(key=lambda item: item[0])                 # A,B,C,...,Z
# print(Students)                                       # [('Ali', 17.5), ('Fatime', 19.5), ('Mariam', 18.5), ('Reza', 15.5), ('Sogol', 11.5)]



Students = [("Ali", 17.5), ("Mariam", 18.5), ("Reza", 15.5), ("Fatime", 19.5), ("Sogol", 11.5),]

# Map
Names = []
for name, _ in Students:
    Names.append(name)
# print(Names)                #['Ali', 'Mariam', 'Reza', 'Fatime', 'Sogol']

Names = map(lambda item: item[0], Students)
# for name in Names:
#     print(name)
# print(Names)

Names = list( map(lambda item: item[0], Students) )

# print(Names)

TopStudent = []
for student in Students:
    if student[1] >= 17:
        TopStudent.append(student)
# print(TopStudent)           #[('Ali', 17.5), ('Mariam', 18.5), ('Fatime', 19.5)]

TopStudent = list(filter(lambda item: item[1] >= 17, Students))
print(TopStudent)             #[('Ali', 17.5), ('Mariam', 18.5), ('Fatime', 19.5)]



