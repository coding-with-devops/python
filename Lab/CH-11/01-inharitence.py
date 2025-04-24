class employee:
    company = "Google"
    name = "Ashutosh"
    salary = 1200000
    def getinfo(self):
        print(f" {self.name} is working on {self.company} and his salary is : {self.salary} ")
        return

class employee_data(employee):
    def GetSalary(self):
        print(f" {self.name}'s salary is : {self.salary} ")

data = employee_data()
data.getinfo()
data.GetSalary()