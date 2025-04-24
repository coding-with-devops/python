## Multiple Inheritance occurs when the child class inherits from more than one parent classes.
class employee:
    company = "LTImindtree Limited"
    def show(self):
        print(f"My Company Name is {self.company}")

class developes(employee):
    language = "Python"
    def showdata(self):
        print(f"My Company : {self.company} and Working on {self.language} coder")

class hr_details(developes):
    salary = 120000000
    def showdetails(self):
        print(f"My Company is {self.company} and I am working as a {self.language} developer, I am getting Salary {self.salary}")

a = developes()
a.showdata()
b = hr_details()
b.show()
b.showdata()
b.showdetails()