from random import randint
class employee:
    def __init__(self,name,role="employee"):
        self.name=name
        print(f"{name} is {role} !")
    def showDetails(self,emp_id,salary,department):
        self.emp_id=emp_id
        # self.name=name
        self.salary=salary
        self.department=department
        print(f"Details of {self.name}-\n \tId : {self.emp_id}\n \tSalary : {self.salary}\n \tDepartment : {self.department}")

    def calculateSalary(self,salary):
        self.salary=salary
        total_salary=self.salary+randint(500,2000)
        print(f"Total salary of {self.name} : {total_salary} ")

    def updateSalary(self,increment):
        self.increament=increment
        print(f"salary of {self.name} is updated from {self.salary} to {self.salary+increment}")


class manager(employee):
    team_size=randint(4,11)
    bonus=randint(2000,4000)
    def __init__(self,name,role="manager"):
        print("\n")
        super().__init__(name,role)
        print(f"number of members in the team of {self.name} is {self.team_size}")
    def showDetails(self, emp_id, salary, department):
        return super().showDetails(emp_id, salary, department)
    
    def projectName(self,projectname):
        self.projectNname=projectname
        print(f"{self.name}'s project name is {projectname}")

    def calculateSalary(self):
        print(f"Bonus salary of {self.name} is {self.bonus}")
        print(f"Total salary of {self.name} is {self.salary + self.bonus}")


        

a=employee("alice")
a.showDetails(101,40000,"IT")
a.calculateSalary(40000)
a.updateSalary(5500)


b=manager("peter")
b.showDetails(110,80000,"IT")
b.projectName("Employee management")
b.calculateSalary()

