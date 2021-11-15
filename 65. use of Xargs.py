#use of x argument
#for avoiding of taking more arguments or parameter in function
'''
def student(id, name, sub):
    print(id, name, sub)

student(21, "Mina", "eng" )
'''
def student(*details):
    print(details)

student(21, "Mina", "eng" )

#addition
def addition(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print(sum)
addition(3,4)
addition(3,4,5,6,7,8,9)
addition(9,0,45,2)