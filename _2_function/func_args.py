# -*- coding: utf-8 -*-


# default argument
def power(x, y=1):
    if y <= 0:
        return 1
    else:
        result = x
        count = y
        while count > 1:
            result = x * result
            count = count - 1
        return result


print(power(2, 10))
print(power(2, 0))
print(power(2, y=1))
print(power(2))


# variable parameters
def cal_sum(*numbers):
    sum = 0
    for i in numbers:
        sum = i + sum
    return sum


numbers = (1, 2, 3, 4, 5)
print(cal_sum(*numbers))


# named parameters
def show(name, age=18, **kwargs):
    print('name = ', name, ', age = ', age)
    if kwargs is not None:
        for key in kwargs:
            print(key, ' = ', kwargs[key])


person_info = {'address': 'USA', 'salary': 10000}
show('Tom', **person_info)
show('Mary')
