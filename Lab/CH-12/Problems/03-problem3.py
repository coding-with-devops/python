## Write a list comprehension to print a list 
# which contains the multiplication table of a user entered number.

number = int(input("Enter the Number :"))

multitable = [ number * i for i in range(1,11) ]

print(multitable)
#for i, item in enumerate(multitable):
#    print(f"{i+1}x{number}= {item}")