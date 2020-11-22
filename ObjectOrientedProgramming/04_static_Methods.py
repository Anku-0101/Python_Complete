'''
Sometimes we need a function that doesn't use the self parameter. We can define a 
static method like for them by using the @static method decorator
'''

class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

harry = Employee()
harry.salary = 500000
harry.getSalary() # This is equivalent to Employee.getSalary(harry)
harry.greet()
