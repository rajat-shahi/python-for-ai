# parent class : general animal
class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"

# child class : dog

class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!!"


# create a dog : using positional argument
my_dog = Dog("Buddy")

# or with named argument
my_dog2 = Dog(name="Max")

# Dog can do animal things (inherited)
print(my_dog.eat()) # Buddy is eating
print(my_dog.sleep()) # Buddy is sleeping
print(my_dog.bark())
print(my_dog2.bark()) # dog can also do dog things
print(my_dog2.sleep())