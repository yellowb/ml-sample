# -*- coding: utf-8 -*-

class Human:

    species = 'Human'  # class level

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def speak(self):
        print('I am a human, my name is %s, %d years old.' % (self.__name, self.__age))

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    # class level function
    @staticmethod
    def get_species():
        return Human.species
