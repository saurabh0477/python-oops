class Employee:
    def info(self,name,salary):
        self.name=name
        self.salary=salary
        print(self.name,self.salary)

    @staticmethod #Creating a static methood
    def greet(): 
        print("Good morning ")

obj1=Employee()
obj1.info("Saurabh",40000)
obj1.greet()   # Call static method using object

'''Static methods are used when a function:

         -> is related to the class
         -> but does not depend on object attributes'''