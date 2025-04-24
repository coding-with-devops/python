# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    
ashutosh = Programmer("Ashutosh", 12000000, 758047)
p2 = Programmer("Rocky", 19000000, 751024)
##print(ashutosh.name,ashutosh.salary)
print(f"Hi {ashutosh.name}, \n Your Salary: {ashutosh.salary}\n Your Pincode:{ashutosh.pin} \n Company Name: {ashutosh.company} ")
print(f"Hi {p2.name}, \n Your Salary: {p2.salary}\n Your Pincode:{p2.pin} \n Company Name: {p2.company} ")

'''
for i in range(1,3):
    name = input("Enter Empoyee Name:")
    salary = int(input("Enter Salary :"))
    pincode = int(input("Enter Pincode:"))
    p[i] = Programmer(name,salary,pincode)
    
print(f"Hi {p2.name}, \n Your Salary: {p2.salary}\n Your Pincode:{p2.pin} \n Company Name: {p2.company} ")
'''