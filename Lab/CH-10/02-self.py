class employee:
    company = "Google"
    name = "Ashutosh"
    salary = 1200000
    def getinfo(self):
        print(f" {self.name} is working on {self.company} and his salary is : {self.salary} ")
        return

my_data = employee()
#print(my_data.company, my_data.salary)
my_data.getinfo()
employee.getinfo(my_data)