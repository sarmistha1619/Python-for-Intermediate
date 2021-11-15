#recursion:calls itself

def fact(n):
    if n==0 or n==1:
        return 1
    #as only the positive int have the factorial value
    elif n>1:
        return n*fact(n-1)
print(fact(3))
print(fact(5))
print(fact(0))
print(fact(1))