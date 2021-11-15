# it returns iterable objects/elements,
# this is why we present those as list
# has two parameters

#map(function, iterable object)

def sq(x):
    return x*x

l=[1,2,3,4]
m=map(sq, l)
l2=list(m)
print(l2)

#another use for taking user input
#1
m=map(int, input().split())
l3=list(m)
print(l3)

#2
m=map(str, input().split())
l3=list(m)
print(l3)

#3
m=map(float, input().split())
l3=list(m)
print(l3)