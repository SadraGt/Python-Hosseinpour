number = int(input("Enter Number :"))

for i in range (2,number):
    x = number % i 
    if x == 0:
        print(f"{number} is not prime! ")
        break
    else:
        print(f"{number} is a prime number ")
        
