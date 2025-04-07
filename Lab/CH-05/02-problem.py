#Write a program to input eight numbers from the user and display all the unique numbers (once).


unique_numbers = set()

for i in range(8):
    number = int(input(f"Enter a number {i + 1}: "))
    unique_numbers.add(number)
print("Unique numbers are:", unique_numbers)