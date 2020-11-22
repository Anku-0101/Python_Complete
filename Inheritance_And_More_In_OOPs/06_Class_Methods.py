'''
Class Methods
A class method is a method which is bound to the class and not the object of the class.
@ classmethod decorator is used to create a class method

'''

class Employee:
    company = 'Kindle'
    salary = 100
    location = 'Delhi'

    # def chnageSalary(self, sal):
    #   self.__class__.salary = sal

    @classmethod
    def chnageSalary(cls, sal):
        cls.salary = sal
    

e = Employee()
print(e.salary)
e.chnageSalary(455)
print(e.salary)
print(Employee.salary)