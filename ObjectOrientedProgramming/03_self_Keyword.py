'''
Self refers to the instance of the class. It is automatically passed with a function call
from an object

'''

class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")
    

harry = Employee()
harry.salary = 300000
harry.getSalary() # This is equivalent to Employee.getSalary(harry)
# Because of that this line throws an error
harry.getDetails() 
