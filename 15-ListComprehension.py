Students = [("Ali", 17.5), ("Mariam", 18.5), ("Reza", 15.5), ("Fatime", 19.5), ("Sogol", 11.5),]

NameStudents = [stuN[0] for stuN in Students]
print(NameStudents)
TopStudents = [stuT[1] for stuT in Students if stuT[1] >= 17]
print(TopStudents)
