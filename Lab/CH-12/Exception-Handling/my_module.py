
def Func():
    print("This Is Module")
Func()
if __name__ == "__main__":
    print("We are directly execute from file. Cant import to other")
    Func()
    print(__name__)
    