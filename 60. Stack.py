#creating a list
#push
name=[]
name.append("mina")
name.append("raju")
name.append("mithu")
name.append("rocky")
print(name)

#pop
name.pop()
name.pop()
print(name)
print("the last name is:", name[-1])
name.pop()
name.pop()
name.pop()

#for avoiding the error
if not name:
    print("There is no name now.")