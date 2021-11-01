student = {
    11:"Mina",
    12:"Raju",
    13:"Mithu"
}

print(student)
print(student[12])

print(student.get(12))
print(student.get(15))
print(student.get(15,"here is no value of 15"))
print(student.get(12,"here is no value of 12"))