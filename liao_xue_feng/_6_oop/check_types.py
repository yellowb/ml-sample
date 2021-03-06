import types
from liao_xue_feng._6_oop.human import Human
from liao_xue_feng._6_oop.student import Student

# simple types
print(isinstance(123, int))
print(isinstance(12.3, float))
print(isinstance('abc', str))

none_value = None
print(none_value is None)

# complex types
print(isinstance(abs, types.BuiltinFunctionType))
print(isinstance(abs, types.FunctionType))  # False, built-in function is not function =_=
print(isinstance(Human.speak, types.FunctionType))
print(isinstance(lambda x: x + 1, types.LambdaType))
print(isinstance((x for x in range(10)), types.GeneratorType))
print(isinstance([x for x in range(10)], list))
print(isinstance([1, 2, 3], (list, tuple)))

# user defined class
tom = Student('tom', 100, 'IT')
print(isinstance(tom, Human))  # True

# list all attr of an object
print(dir(tom))


