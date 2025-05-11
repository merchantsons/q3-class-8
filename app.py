# Note: This simple code demonstrates all four pillars of Object-Oriented Programming in Python: Encapsulation, Abstraction, Inheritance, and Polymorphism.
# Written by Merchantsons - GIAIC ROLL # 00037391

from abc import ABC, abstractmethod

# Abstraction
class Animal(ABC):
    def __init__(self, name):
        self.name = name  # Encapsulation

    @abstractmethod
    def make_sound(self):
        pass

    def get_name(self):
        return self.name

# Inheritance
class Dog(Animal):
    def make_sound(self):  # Polymorphism
        return "Woof!"

# Inheritance
class Cat(Animal):
    def make_sound(self):  # Polymorphism
        return "Meow!"

# Client code
def animal_sounds(animals):
    for animal in animals:
        print(f"{animal.get_name()} says {animal.make_sound()}")

# Creating instances
dog = Dog("Pluto")
cat = Cat("whiskers")

# Using the instances
animals = [dog, cat]
animal_sounds(animals)
