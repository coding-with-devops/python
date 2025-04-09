# Write a function with factorial(n) = n x factorial (n-1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
n = int(input("Enter the Number :"))
print(f"Factorial of {n} : {factorial(n)}")