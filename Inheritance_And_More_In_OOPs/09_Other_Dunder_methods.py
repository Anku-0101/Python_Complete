class Number:
    def __init__(self, num): 
        self.num = num
    
    def __add__(self, num2): # To overload + use __add__ dunder method
        print("Lets add")
        return self.num + num2.num
    
    def __mul__(self, num2): # To overload * Operator use __mul__ dunder method
        print("Lets multiply")
        return self.num * num2.num
    
    def __str__(self):
        return f"Decimal Number {self.num}"
    
    def __len__(self):
        i = 0 
        j = 0
        
        if(self.num < 0):
            j = -self.num

        else :
            j = self.num

        while j > 0 :
            j = j//10
            i = i+1
        
        return i


n = Number(955)
print(n)   # Without str dunder method we get memory location of object n
print(len(n))