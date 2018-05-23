import json

"""Demo of serialization and deserialization using JSON"""

# Serialize a dict
dict_obj = {
    'name': 'Tom汤姆',
    'age': 22,
    'likes': ['dog', 'cat']
}

json_str = json.dumps(dict_obj)
print(json_str)

dict_obj_2 = json.loads(json_str)
print(dict_obj_2)


# Serialize a class object
class Man:
    def __init__(self, name, age, *likes):
        self.name = name
        self.age = age
        self.likes = likes


man = Man('Tom汤姆', 22, 'dog', 'cat')

# solution 1: use __dict__
json_str = json.dumps(man.__dict__)
print(json_str)


# solution 2: define a convert function
def man_to_dict(man):
    return {
        'name': man.name,
        'age': man.age,
        'likes': man.likes
    }


json_str = json.dumps(man, default=man_to_dict)
print(json_str)


