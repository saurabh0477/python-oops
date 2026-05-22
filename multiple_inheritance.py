#Multiple inheritance

class addition:
    def add(self,number1,number2):
        self.number1=number1
        self.number2=number2
        print(f"addition of {number1} and {number2} : {number1+number2}")


class multiplication:
    def mult(self,number1,number2):
        self.number1=number1
        self.number2=number2
        print(f"Multiplication of {number1} and {number2} : {number1*number2}")


class calculator(addition,multiplication): #Inherit class addition and multiplication
    def square(self,number1):
        self.number1=number1
        print(f"Square of {number1} : {number1*number1}")

check=calculator() #Creating object of class calculator 
check.add(2,4) #using methods
check.mult(2,3)
check.square(5)

'''We can use methods of class addition and multiplication by creating object of class calculator because it inherited both classes '''