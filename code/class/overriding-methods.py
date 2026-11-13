class Animal:
    def __init__(self,name):
        self.name = name 

    def makes_sound(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def makes_sound(self):
        return f"{self.name} barks : woof!!"

class Cat(Animal):
    def makes_sound(self):
        return f"{self.name} meows : meow !!"

dog = Dog(name="Buddy")
dog.makes_sound()

cat = Cat(name="Billa")
cat.makes_sound()