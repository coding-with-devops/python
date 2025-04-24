# Create a class ‘Employee’ and add salary and increment properties to it.
#Write a method ‘salaryAfterIncrement’ method with a @property decorator 
# with a setter which changes the value of increment based on the salary.

class Employee:
    salary = 120000
    increment = 10

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self.increment = ((value/self.salary) - 1) * 100
    

a = Employee()
print(a.increment, a.salaryAfterIncrement)
a.salaryAfterIncrement = 150000
print(a.salaryAfterIncrement, a.increment)

        