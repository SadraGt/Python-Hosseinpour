from locationclass19 import Location

L1 = Location(20, 40)
L4 = Location(20, 40)

L5 = L1 + L4        # L5 = L1.__add__(L4))
L6 = L1 - L5        # L5 = L1.__sub__(L5))
print (L1 == L4)    # L1.__eq__(L4))
print (L1 < L5)     # L1.__gt__(L5))
print (L5.show())   
print (L6.show())
