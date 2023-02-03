# ax^2 + bx + c = 0
# delta = b^2 -4ac
# if delta < 0    -->     no root
# if delta == 0   -->     one root   -->     -b/2a
# if delta < 0    -->     two root   -->     (-b +- sprt(delta)) / 2
#-----------------------------------------------------------------------

# import math


# def ax (a,b,c):
#     Delta = b^2 - (4*a*c)
#     if Delta < 0 :
#         print("no have root !!")
#     if Delta == 0 :
#         x = -b / (2*a)
#         print(f"We have one root \nroot is : {x}")
#     else:
#         x = (-b + math.sqrt(Delta)) / (2*a)
#         y = (-b - math.sqrt(Delta)) / (2*a)
#         print(f"We have two root \nroot is : {x} and : {y}")


# a = int(input ("ax^2 + bx + c = 0 \na= "))
# b = int(input ("b= ") )
# c = int(input ("c= ") )

# ax (a,b,c)

import math

def Solve (a,b,c):
    Delta = b^2 - (4*a*c)
    if Delta < 0 :
        return 0 , None , None
    if Delta == 0 :
        x = -b / (2*a)
        return 1 , x , None
    else:
        x = (-b + math.sqrt(Delta)) / (2*a)
        y = (-b - math.sqrt(Delta)) / (2*a)
        return 2 , x , y 

def PSolve (a,b,c):
    if a == 0 :
        print ("We don't have root!")
    elif a == 1 :
        print (f"Root is : {b:.5f} ")
    else:
        print (f"Root1 is : {b:.5f}\nRoot2 is : {c:.5f}")

a = int(input ("ax^2 + bx + c = 0 \na= "))
b = int(input ("b= ") )
c = int(input ("c= ") )
RootCount, Root1, Root2 = Solve(a,b,c)
PSolve(RootCount,Root1,Root2)