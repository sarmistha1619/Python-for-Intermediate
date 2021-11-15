#use of xx arguments
#works like dictionary
# use ** for xx args

def students(**details):
    print(details)

students(id=10, name="Sarah", sub= "English")
print(students["id"])