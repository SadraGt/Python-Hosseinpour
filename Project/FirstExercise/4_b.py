while True:

    number = int(input("Enter Number:   Enter -1 for exit"))
    if number == -1:
        break

    a=0
    b=1
    if number == 0:
        print (0)
    if number == 1:
        print (1)

    else:
        print (0)
        print (1)
        for i in range(1 , number):
            c = a + b
            print (c)
            a = b
            b = c

