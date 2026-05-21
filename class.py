class Employee: #Employee is a class
    lang="py"   #This is a class attribute
    salary=40000

    def getInfo(self):  #getInfo is a method
        print(f"The language is {self.lang}. The salary is {self.salary}")
    


flash=Employee()  #Object
flash.name="Flash"  #this is instance attribute
print(flash.name,flash.lang,flash.salary)

peter=Employee()  #Object
peter.name="Peter" 
peter.lang="Java" #instance attribute overriding class attribute
print(peter.name,peter.lang,peter.salary)