#FIFO
#if we code by using list, the element have to be moved

#by using dequeue
from collections import deque
bank=["a","b","c"]
b=deque(bank)
print(b)

b.popleft()
b.popleft()
print(b)

b.append("d")
b.append("e")
b.append(14)
b.append(12)
print(b)
