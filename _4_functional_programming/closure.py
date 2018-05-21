# sample for closure


def count(n):
    return lambda: sum(range(1, n + 1))


f2 = count(5)
print(f2())  # lazy execute
