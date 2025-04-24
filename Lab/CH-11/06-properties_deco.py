class employee:
    def __init__(self, my_name):
        self.my_name = my_name
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

a = employee("Ashutosh Muduli")
a.name = "Ashutosh Muduli"
print(a.name)
print(a.fname)