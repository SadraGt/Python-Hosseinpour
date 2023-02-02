def Convert(Number):
    x = Number
    z = ""

    while x != 0:
        z = str(x % 2) + z  
        x = x // 2
    print(z)

Convert(19)