'''
Solving a problem by creating objects is one of the most popular approaches in programming. 
This is called object oriented programming.

This concept focuses on using reusable code. Implements DRY(don't repeat yourself) principle
'''


'''
Class
A class is a blue print for creating objects. eg - A railway reservation form 

Object
An object is an isntantiation of a class. When class is defined, a template (info) is defined.
Memory is allocated only after object instantiation.

Objects of a given class can invoke the methods available to it without reading the implementation
details to the user, --> Abstraction and Encapsulation

'''


'''
Modelling a problem in OOPs
We identify the following in our problem 

Noun            -->     Class       -->     Employee
Adjective       -->     Attributes  -->     name, age, salary
Verbs           -->     Methods     -->     getSalary(), increment()
'''

'''
Class Attributes
An attribute that belongs to the class rather than a particular object.

Example:
    Class Employee:
        company = "Google"          --> [Specific to each class]

    harry = Employee()
    harry.company -> Google
    Employee.company = "Microsoft"  --> [Changing class attribute]
'''
# Procedural oriented programming
a = 12 
b = 34
print("The sum of a and b is", a+b)

# OOPs 

class Number:
    def sum(self):
        return self.a + self.b 

num = Number()
num.a = 12
num.b = 30
s = num.sum()
print("The sum is ", s)

