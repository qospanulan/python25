from abc import ABC


class Animal(ABC):

    @classmethod
    def say_something(cls):
        print("R-r-r")


class Cat(Animal):

    @classmethod
    def say_something(cls):
        print("Было:")
        super().say_something()

        print("Стало:")
        print("Myau-myau")

class Dog(Animal):
    pass


c = Cat()
d = Dog()

print("cat:")
c.say_something()
# print("dog:")
# d.say_something()

