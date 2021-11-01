#unordered collection of items
#duplicate items are not print in the output
#can't be accessed by index


#print
numbers1 = {1,2,3,4,6,7,9}
print(numbers1)

#duplicate items are not print in the output
numbers2 = {1,2,3,4,4,4,6,7,9}
print(numbers2)
#print(numbers2[2])

#convert list to set
l=[1,2,4,"Mina", 6]
s=set(l)
print(s)

#convert list to set 2
print(set([1,2,4,"Mina", 6]))

#add element
s.add(8)
print(s)

#REMOVE element
s.remove(4)
s.remove("Mina")

#use of in and not in
print(s)
print(2 in s)
print(2 not in s)
print(3 not in s)
print(3 in s)