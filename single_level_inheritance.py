#Single level inheritance
class first:
    def add(self,a,b):
        print("this is a first class")
        self.a=a
        self.b=b
        print(a+b)

class second(first): 
    def show(self):
        print("this is a second class") 

check=second()
check.add(28,6)
check.show()

#we does not create any object of class first still we can use method of that class by creating the object of second class with the help of inheritance
