class Vector:
    def __init__(self, vector_):
        self.vec = vector_
    
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]
    
    def __add__(self, vec2):
        if(len(vec2.vec) != len(self.vec)):
            return "Addition not possible for vectors having different dimensions"

        else:
            result = []

            for i in range(len(self.vec)):
                result.append(self.vec[i] + vec2.vec[i])
            return Vector(result)
    
    def __mul__(self, vec2):
        if(len(vec2.vec) != len(self.vec)):
            return "Dot Product not possible for vectors having different dimensions"
        
        else:
            sum = 0
            for i in range(len(self.vec)):
                sum += self.vec[i] * vec2.vec[i]
            return sum
    
    def __len__(self):
        return len(self.vec)

v1 = Vector([1, 5])
v2 = Vector([0, 3])
v3 = Vector([7, 5, 3])
v4 = Vector([1, 0, 7])

print(v1)
print(v3)

print(len(v1))
print(len(v3))

print(v1+v2)
print(v1*v2)
print(v3+v2)
print(v3*v4)
print(v1+v3)
print(v1*v3)