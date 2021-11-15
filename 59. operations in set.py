#union
set1 = {1,3,5,6,7, 34,23}
set2 = {3,5,1,6,7,8, 11, 14}
print(set1|set2)
print(set1.union(set2))

#intersection
print(set1&set2)
print(set1.intersection(set2))

#differance
print(set1-set2)
print(set1.difference(set2))