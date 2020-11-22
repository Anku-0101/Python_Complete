'''
__init__() is a special method which is first run as soon as the object is created.
__init__() method is also known as constructor

It takes self argument and can also take further arguments 
'''

class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")


    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")
    

harry = Employee("Harry", 7800014, "YouTube")
harry.getDetails()