# 다향성

class Animal:
    def __init__(self,name):
        self.name=name
    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method') #추상메서드

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof Woof!'

animals=[Cat('Missy'),Cat('Mr.mistoffelees'),Dog('zion')]

for animal in animals:
    print(animal.name+':'+animal.talk())