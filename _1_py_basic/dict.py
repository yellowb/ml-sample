# -*- coding: utf-8 -*-

# a simple dict
dict = {}
dict['yellow'] = 100
dict['blue'] = 99
dict[100] = 100

print(dict)

for o in dict:
    print('key = %s, value = %s' % (o, dict[o]))

# use get() to avoid error if key not existed
print(dict.get('yellow'))
print(dict.get('null'))  # return None
print(dict.get('null', 0))  # return 0

# remove a key
dict.pop(100)
print(dict)

