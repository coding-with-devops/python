# Calculatore with Match Case
n1 = int(input("Enter Your 1st Number:"))
n2 = int(input("Enter Your 2st Number:"))
print(''' Please Enter Your Choice from 1-4
            1. Add
            2. Sub
            3. Multiplication
            4. Division''')
select = int(input("Enter Your Choice [1/2/3/4]:"))
match select:
    case 1:
        print("Sum result:", n1 + n2)
    case 2:
        print("Sub result:", n1 - n2)
    case 3:
        print("Multiply result:", n1 * n2)
    case 4:
        if ( n2 != 0):
            print("Division result:", n1 / n2)
        else:
           print("Error: Division by zero")
    case _:
        print("Invalid Choice")
