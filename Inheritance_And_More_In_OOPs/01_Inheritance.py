'''
Inheritance is a way of creating a new class from an existing class

'''
class Employee:
    company = 'Google'

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = 'Java'

    def getLanguage(self):
        print(f"The language is {self.language}")
    
    def showDetails(self):
        print("This is an programmer")
    
e = Employee()
e.showDetails()

p = Programmer()
p.showDetails()
