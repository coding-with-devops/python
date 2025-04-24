class employee:
    company = "ITC Infotech"
    name = "Ashutosh"
    def show(self):
        print(f"{self.name} is working on {self.company}")
class coders:
    language = "Python"
    def showlang(self):
        print(f"Out of All Language here is your is {self.language}")
class programmer(employee, coders):
    def showall(self):
        print(f" {self.name}'s Company is {self.company} and he is working as {self.language} Develeoper")

a = employee()
b = coders()
c = programmer()
a.show()
c.show()
c.showlang()
c.showall()