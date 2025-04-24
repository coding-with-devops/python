class employee:
    a = 4
    @staticmethod
    def greet():
        print("Welcome !!!")
    @classmethod
    def show(self,func):
        func()
        print(f"Class value is {self.a}")
e = employee()
e.a = 45
e.show(e.greet)