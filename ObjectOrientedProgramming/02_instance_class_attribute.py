class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
# If the instance is present in object then that value is taken if not then the value from class is taken
# If the instance isn't present in both object and class then an error is thrown


harry.salary = 450
print(harry.salary)
print(rajni.salary)

# Below line throws an error as the instance address is not present in both object and class harry
print(harry.address)