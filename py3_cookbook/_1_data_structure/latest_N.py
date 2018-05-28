""" How to get the latest N elements from input """

from collections import deque

q = deque(maxlen=3)

q.append(1)
q.append(2)
q.append(3)
print(q)

# will pop the 1st element
q.append(4)
print(q)
