# Entity موجودیت
# 1-Propertises 2-Behavior 

from locationclass19 import Location

L1 = Location(20, 40)
L2 = Location(8)
L3 = Location()
L4 = Location(20, 40)
L1.show()

print (L1.distance())
L3.y = -50
print (L1.distance(L3))

print (L1 == L4)

#L5 = L1 + L2 ❌
