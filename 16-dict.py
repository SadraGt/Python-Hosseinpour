# key = value 

point1 = {'x':10, 'y':20}
point2 = dict(x=10, y=20)

# print(point1)     # {'x': 10, 'y': 20}
# print(point2)     # {'x': 10, 'y': 20}

point1['x'] = 15    
point1['z'] = 25    

# print(point1)         # {'x': 15, 'y': 20, 'z': 25}
# print(point2['y'])    # 20

# if 'w' in point1:
    # print(point1['w'])
# else:
    # print('w not in point1')  # w not in point1

# print(point1.get('w', None))  # None

Students = dict(Ali = 18, Nazanin = 20, Riza = 16, Nahid = 15)

# for s in Students:
#     print(f"{s} Average is :{Students[s]}")
# Or
for name, avg in Students.items():
    print(f"{name} Average is :{avg}")