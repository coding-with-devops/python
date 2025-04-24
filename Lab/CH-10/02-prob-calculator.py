# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self,n):
        self.n = n

    @staticmethod
    def greet():
        print("Hello There")

    def square(self):
        print(f"The square of {self.n} : {self.n * self.n}")
    
    def cube(self):
        print(f"The Cube of {self.n} : {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"The squareroot of {self.n} : {round((self.n ** (1/2)),3) }")
  



a = Calculator(3)
a.greet()
a.square()
a.cube()
a.squareroot()
Calculator.squareroot(a)