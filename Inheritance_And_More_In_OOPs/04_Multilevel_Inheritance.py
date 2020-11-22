class person:
    country = "India"
    Name = "Aman"

    def DateOfBirth(self):
        print("Date of birth dd/mm/yyyy")
    
    def NetWorth(self):
        print("Net worth is 0")


class Employee(person):
    company = "Honda"
    salary = "5814"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def NetWorth(self):
        print("Net worth is ", self.salary)

class programmer(Employee):
    company = "Fiberr"

    def getSalary(self):
        print("Salary is $787878787878")


p = person()
p.DateOfBirth()
e = Employee()
e.salary = 478778
pr  = programmer()
pr.NetWorth()