from collections import namedtuple, deque, defaultdict, OrderedDict

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

# default dict
dd = defaultdict(lambda: 0)
print(dd['NotExist'])  # prints 0

# ordered dict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
for k, v in od.items():
    print("%s -> %s" % (k, v))





