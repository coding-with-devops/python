def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, %, **")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /, %, **): ")
        num2 = float(input("Enter second number: "))

        match operator:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '*':
                result = num1 * num2
            case '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    return "Error: Division by zero"
            case '%':
                result = num1 % num2
            case '**':
                result = num1 ** num2
            case _:
                return "Invalid operator"

        return f"Result: {result}"

    except ValueError:
        return "Invalid input. Please enter numeric values."

# Run the calculator
print(calculator())
