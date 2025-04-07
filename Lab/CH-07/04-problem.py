#Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter a number: "))

i = 1
sum = 0
while i <= n:
    sum = sum + i
    i += 1
print(f"The sum of first {n} natural numbers is: {sum}")

#Write a program to calculate the factorial of a given number using for loop.

j = 1
factorial = 1
while j <= n:
    factorial = factorial * j
    j += 1
print(f"The factorial of {n} is: {factorial}")