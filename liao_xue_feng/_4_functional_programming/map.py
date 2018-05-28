# sample of built-in map function


def square(x):
    return x * x

data = list(range(11))
print(data)

# returns the square value of each element in original list
itor = map(square, data)  # `map` returns an iterator(lazy)
new_data = list(itor)  # immediately calculate all elements

print(new_data)
