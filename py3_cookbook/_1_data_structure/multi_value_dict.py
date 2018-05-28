from collections import defaultdict

""" Sample to generate a multiple value dictionary """

d = defaultdict(list)
d['key'].append(1)
d['key'].append(2)
d['key'].append(3)

print(d['key'])
