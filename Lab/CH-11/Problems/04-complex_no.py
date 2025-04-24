class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary        

    def __add__(self, complex_no):
        return Complex(self.real + complex_no.real, self.imaginary + complex_no.imaginary)
    
    def __mul__(self, scalar):
        real_part = (self.real *  scalar.real) - (self.imaginary * scalar.imaginary)
        imaginary_part = (self.real * scalar.imaginary) + (self.imaginary * scalar.real)
        return Complex(real_part, imaginary_part)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    
c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1 + c2 )
print(c1 * c2)