""" Assign a list to multiple variables """

x, y = [1, 2]
print(x, y)

name, age, weight, (year, month, day) = ['ACME', 50, 91.1, (2012, 12, 21)]
print(name, age, weight, year, month, day)

# if you want to ignore some of them
name, age, _, _ = ['ACME', 50, 91.1, (2012, 12, 21)]
print(name, age)

