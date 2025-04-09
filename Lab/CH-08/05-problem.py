#Write a python function to print multiplication table of a given number.

def multi_table (number):
    for i in range(10):
        print(f"{i+1} x {number} = ", (i+1) * number)

num = int(input("Enter The Number :"))

multi_table(num)