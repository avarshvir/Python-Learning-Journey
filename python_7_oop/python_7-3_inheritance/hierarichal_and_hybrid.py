class Animal:
    def animal_fun(self):
        print("This is Animal class")

class Dog(Animal):
    def dog_fun(self):
        print("This is Dog class")

class Wolf(Animal):
    def wolf_fun(self):
        print("This is Wolf class")

class Husky(Dog,Wolf):
    def husky_fun(self):
        print("This is Husky class")

h1 = Husky()
h1.animal_fun()
h1.dog_fun()
h1.wolf_fun()
h1.husky_fun()

