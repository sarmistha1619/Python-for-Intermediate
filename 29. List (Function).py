l = ["cat", "pen", "book", 23 , 10, 10, 10]

l.append("water")
l.insert(3, "food")
l.remove("book")
print(l)
l.reverse()
print(l)

b= [10,42, 12,32]
b.reverse()
print(b)
b.pop()
print(b)

a = b.copy()
print(a)

a.clear()
print(a)

c = l.count(10)
print(c)