# sample of built-in reduce function
# DIY function to convert string to number


from functools import reduce


def char_to_digit(c):
    mapping = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    return mapping[c]


def accumulate(x, y):
    if isinstance(x, str):
        x = char_to_digit(x)
    if isinstance(y, str):
        y = char_to_digit(y)
    return x * 10 + y


str_data = '12345'
int_data = reduce(accumulate, str_data)

print(int_data)
