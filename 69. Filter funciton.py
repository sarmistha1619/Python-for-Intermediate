#works with lists
#has two parameter

#get the even numbers
def number(n):
    return n%2==0
l=[1,2,3,4,5,6,7,8,9,10]

f=filter(number, l)
l2=list(f)
print(l2)

#do all of thic in one line(using Lambda function)
print(list(filter(lambda n:n%2==0,l)))
#get the add numbers
def number(n):
    return n%2==1
l=[1,2,3,4,5,6,7,8,9,10]

f=filter(number, l)
l2=list(f)
print(l2)

#do all of thic in one line(using Lambda function)
print(list(filter(lambda n:n%2==1,l)))