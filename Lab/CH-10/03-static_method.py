class employee:
    company = "Google"
    name = "Ashutosh"
    salary = 1200000
    @staticmethod
    def getinfo():
        print(f" {employee.name} is working on {employee.company} and his salary is : {employee.salary} ")
        return

my_data = employee()
#print(my_data.company, my_data.salary)
my_data.getinfo()