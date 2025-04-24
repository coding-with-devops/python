## Multiple Inheritance occurs when the child class inherits from more than one parent classes.
class employee:
    company = "LTImindtree Limited"
    def __init__(self):
        print(f"My Company Name is {self.company}")

class developes(employee):
    language = "Python"
    def __init__(self):
        print(f"My Company : {self.company} and Working on {self.language} coder")

class hr_details(developes):
    salary = 120000000
    def __init__(self):
        super().__init__()
        print(f"My Company is {self.company} and I am working as a {self.language} developer, I am getting Salary {self.salary}")


#a = developes()
b = hr_details()
