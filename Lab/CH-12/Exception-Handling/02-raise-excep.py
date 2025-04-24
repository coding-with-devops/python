a = int(input("Enter 1st no:"))
b = int(input("Enter 2nd no:"))
if b == 0:
    raise ZeroDivisionError("We cant devide any no by Zero")
else:
    print(f"Division a/b = {a/b}")