#Write a program to print multiplication table of a given number using for loop.

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
else:
    print("Multiplication table completed.")

j = 1
while j in range(1, 11):
    print(f"{number} x {j} = {number * j}")
    j += 1