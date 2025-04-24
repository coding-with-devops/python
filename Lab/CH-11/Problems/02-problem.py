class Animals:
    pass
class Pets(Animals):
    pass
class Dog(Pets):
    @staticmethod
    def show():
        print("Bow Bow !")

a = Dog()
a.show()