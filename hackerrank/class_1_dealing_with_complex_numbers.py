"""
https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

"""
class Complex:

    def __init__(self, real, imaginary):
        self.value = eval(f'{real} + {imaginary}j')
    
    def parse_result(self):
        self.real = self.result.real
        self.imaginary = self.result.imag
        return self.__str__()
        
    def __add__(self, other):
        self.result = self.value + other.value
        return self.parse_result()
        
    def __sub__(self, other):
        self.result = self.value - other.value
        return self.parse_result()
        
    def __mul__(self, other):
        self.result = self.value * other.value
        return self.parse_result()

    def __truediv__(self, other):
        self.result = self.value / other.value
        return self.parse_result()

    def mod(self):
        self.result = abs(self.value)
        return self.parse_result()

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    input1 = '2 1'
    input2 = '5 6'
    c = map(float, input1.split())
    d = map(float, input2.split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
