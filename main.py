import numpy as np

class calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def func_plus(self):
        self.result = self.a + self.b
        return self.result
    
    def func_minus(self):
        self.result = self.a - self.b
    
    def func_multiple(self):
        self.result = self.a * self.b

    def func_divide(self):
        if self.b == 0:
            print("Cannot calculate !")
        else:
            self.result = self.a / self.b
            return self.result

if __name__:
    a = 1
    b = 2
    c = calculator(a, b).func_divide()
    print(c)