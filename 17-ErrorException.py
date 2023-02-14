#Error 

#1-Syntax 
I = 5
# if I = 5:       #    ==
#     print(I)

#2-Semantic
N = 5
F = 0   #  !0  1
for i in range(1,N+1):
    F *= i

# print(F)    #   0 

#3- Run Time , Exception , Logic 

# A = int(input("Enter number : "))
# B = int(input("Enter number : "))

# if B == 0 We have Error and stop python program but We use try and ... for don'n stop program 

# try:
#     C = A / B
#     print(C)
# except:
#     print("Error!!!!")
# else:
#     print("No Error!")
# finally:
#     print("!!!!!!!!!")

# L = [1, 2, 3]
# # print(L[5])     # IndexError: list index out of range
# A = 5
# B = 0
# try:
#     print(L[2])
#     C = A / B
# except IndexError:
#     print("out of range")

# except:
#     print("Error")


def Factoriel(S):       #Robust Function
    # if S < 0 :
    #     raise Exception("Number must be positive")

    if S < 0:
        print("Warinig! your number is negative.")
        S = -S
        
    f = 1
    for i in range(1, S+1):
        f *= i

    return f

# try:
#     O = int(input("Enter number for factoriel: "))
#     M = Factoriel(O)
#     print(f"{O}! = {M}")
# except Exception as ex:
#     print(ex)

