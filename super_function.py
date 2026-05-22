#1. Super() for init 
class grandfather:
    def __init__(self):
        print("This is grandfather class constructer !!")

class father(grandfather):
    def __init__(self): #it overrides the parent's constructer
        super().__init__() #super helps to access parent class constructor
        print("This is father class constructer !!")

class child(father):
    def __init__(self):
        super().__init__()
        print("This is child class constructer !!")

a=child() #child class object


#2. Super() for same method in parent and child

class animal:
    def sound(self):
        print("Animals make sound !!")

class dog(animal):
    def sound(self): #it overrides method sound of class animal
        super().sound() #calling method of animal class with the help of super()
        print("Dog barks !!")

class puppy(dog):
    def sound(self): #it overrides method sound of class dog
        super().sound()  ##calling method of dog class with the help of super()
        print("puppy weeps !!")

tomy=puppy() #object of puppy
tomy.sound() #calling method



