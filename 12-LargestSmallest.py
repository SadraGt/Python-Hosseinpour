def LSNumber(*Number):
    s = Number[0]
    for x in Number:
         if x > s :
            Max = x
         if s > x :
            Max = s
         if x < s :
            Min = x
         if s < x :
            Min = s
    return Max , Min

   

Up , Do = LSNumber(5,9,10,80)
print (f"Your MaxNumber is : {Up} \nYour MinNumber is : {Do}")