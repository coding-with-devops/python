
def sum(a, b):
    sum = a + b
    return sum
def sub(a, b):
    sub = a - b
    return sub
def multi(a, b):
    multi = a * b
    return multi

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

num1 = int(input("Enter the 1st Number:"))
num2 = int(input("Enter the 2nd Number:"))


value = int(input("Enter a your choice 1/2/3: "))
match value:
    case 1:
        print(f"Sum of {num1} and {num2} = ", sum(num1,num2))
    case 2:
        print(f"Substraction of {num1} and {num2} = ", sub(num1,num2))
    case 3:
        print(f"Multiplication {num1} and {num2} = ", multi(num1,num2))
    case _:
        print("Invalid Input")