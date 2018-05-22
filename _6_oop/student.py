# -*- coding: utf-8 -*-
from _6_oop.human import Human


class Student(Human):

    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.__job = job

    def speak(self):
        super().speak()
        print('My job is %s.' % self.__job)
