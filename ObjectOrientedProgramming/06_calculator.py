class calculate:
    def __init__(self, number):
        self.number = number
    
    def Square(self):
        print("The square of the number is ", self.number*self.number)
    
    def SquareRoot(self):
        print("The square root of the number is ", self.number** 0.5)
    
    def Cube(self):
        print("The cube of the number is ", self.number** 3)
    

num = calculate(8)
num.Square()
num.SquareRoot()
num.Cube()

