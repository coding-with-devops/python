class employee:
    company = "Google"
    name = "Ashutosh"
    salary = 1200000
    def __init__(self):
        print(f"Welcome To Employee Portal, \n Hi {employee.name}")
    def getinfo(self):
        print(f" {self.name} is working on {self.company} and his salary is : {self.salary} ")
        return
    @staticmethod
    def greed():
        print("Thank you for Joining. !!!")
my_data = employee()
print(my_data.name, my_data.company, my_data.salary)
my_data.greed()