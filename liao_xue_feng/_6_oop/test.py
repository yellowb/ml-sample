# -*- coding: utf-8 -*-

from liao_xue_feng._6_oop.human import Human
from liao_xue_feng._6_oop.student import Student

tom = Human('Tom', 18)
tom.speak()

tom.__age = 0  # not work, because the `__age` property of Human object had been changed to `_Human__age`
# tom._Human__age = 0  # this will work, but not good
tom.speak()

tom.set_age(0)  # good to use
tom.speak()


tom = Student('Ken', 18, 'IT')
tom.set_age(100)
tom.speak()

print(tom.get_species())
print(Student.get_species())

