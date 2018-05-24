from collections import namedtuple, deque, defaultdict

# use namedtuple to create a named tuple with named properties
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)
print('%d , %d' % (p.x, p.y))

# deque
q = deque([1, 2, 3])
q.append(4)
q.popleft()
print(q)

