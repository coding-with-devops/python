#Check that a tuple type cannot be changed in python.

items = ( "apple", "banana", 22, 45.09, False, 62 , True, "cherry" )
for i in items:
    print(i)  


a = (7, 0, 8, 0, 0, 9)
print(a.count(0))  # Output: 3

number = []
for i in range(4):
    num = int(input(f"Enter a number {i + 1}: "))
    number.append(num)

total = sum(number)
print("Sum of numbers:", total)