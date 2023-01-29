number = int(input("Enter Number :"))
Prime = True
for i in range (2,number):
    x = number % i 
    if x == 0:
        print(f"{number} is not prime! ")
        Prime = False
        break

if Prime == True:
    print(f"{number} is a prime number ")
        