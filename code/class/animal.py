class Dog():
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed 

    def info(self):
        print("Dog Details:")
        print("-"*12)
        print(f"Name : {self.name}")
        print(f"Breed : {self.breed}")


class Cat():
    def __init__(self, name, color):
        self.name = name
        self.color = color 

jerry = Dog(name="Jerry",breed="Labrador")
jerry.info()
jerry.breed


tim = Dog(name="tim",breed=None)
tim.info()