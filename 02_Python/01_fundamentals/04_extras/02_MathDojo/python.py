from unittest import result


class MathDojo:
    
    def __init__(self):
        self.result = 0
    
    
    def add(self, num, *nums):
        self.result = num
        for x in nums:
            self.result += x
        print(self.result)
        self.result = 0 
    
    
    def subtract(self, num, *nums):
        self.result = num
        for x in nums:
            self.result -= x
        print(self.result)
        self.result = 0 



# crear una instancia:
md = MathDojo()

# para probar:
md.add(2,2)
md.add(2,1,5)
md.add(2,1,5,8)

print("\n")
md.subtract(9,2,3)
md.subtract(8,-2)
md.subtract(8,2,1,5)

