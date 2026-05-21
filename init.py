class Employee:  #Employee is class
    def __init__(self): #this is first constructor
        print("This is a constructor..!")

    def __init__(self, name, lang,salary): #this is new constructor and it overwrite previous constructor so only this will be called when object is created
        self.name = name      # Initialize name
        self.lang = lang      # Initialize language
        self.salary = salary  # Initialize salary
        print(f"the salary of {name} is {salary} and he use {lang} language")

obj1=Employee("Alice","Python",40000) #object creation

obj2=Employee("Bob","Java",45000)

