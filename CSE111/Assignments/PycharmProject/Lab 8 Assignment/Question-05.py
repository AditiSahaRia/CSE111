#Task-05
#Author Aditi Saha Ria
#ID : 20101238

class Animal:
    def __init__(self,sound):
        self.__sound = sound

    def makeSound(self):
        return self.__sound
class Printer:
    def printSound(self, a):
        print(a.makeSound())

class Dog(Animal):
    def __init__(self, d):
        self.dog_sound = d
        super().__init__(self.dog_sound)

class Cat(Animal):
    def __init__(self, c):
        self.cat_sound = c
        super().__init__(self.cat_sound)


d1 = Dog('bark')
c1 = Cat('meow')
a1 = Animal('Animal does not make sound')
pr = Printer()
pr.printSound(a1)
pr.printSound(c1)
pr.printSound(d1)