class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1
    
class Employee:
    company = "Visa"
    eCode = 120


class Programmer(Freelancer, Employee):
    name = "Aman"


p = Programmer()
p.upgradeLevel()
print(p.company)   # Company attribute is present in both Freelancer and Employe in this case the class first inherited is taken to be prior than others

