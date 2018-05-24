import itertools

# create an endless iterator
loop = itertools.count(1, 2)
for x in loop:
    if x > 999:
        break
    print(x)

# create an endless cycle
cycle = itertools.cycle(['A', 'B', 'C'])
i = 0
for x in cycle:
    if i > 9:
        break
    print(x)
    i = i + 1

# group same elements from an iterable
groups = itertools.groupby('AAaaabBbCCcccC', key=lambda c: c.upper())
for k, v in groups:
    print(k, list(v))

# filter
odds = itertools.filterfalse(lambda x: x % 2 == 0, list(range(10)))
print(list(odds))
