#Method overriding

class animal:
    def sound(self):
        print("Animals make sound !!")

class dog(animal):
    def sound(self): #it overrides method sound of class animal
        print("Dog barks !!")

class puppy(dog):
    def sound(self): #it overrides method sound of class dog
        print("puppy weeps !!")

tomy=puppy()
tomy.sound()

