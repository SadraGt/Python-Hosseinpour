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
         else:
            Max = s 
            Min = s

    return Max , Min

   

Up , Do = LSNumber(5,5,5,5)
Up1 , _ = LSNumber(55,66,88)  # Only Max We Need
_ , Do1 = LSNumber(789,541,2) # Only Min We Need
print (f"Your MaxNumber is : {Up} \nYour MinNumber is : {Do}")
