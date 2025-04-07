
list1 = [ "Alice", "Bob", "Charlie", "David", "Eve" ]

name = input("Enter a name: ")

if name in list1:
    print(f"{name} is in the list, You can proceed with the next steps.")
    index = list1.index(name)
    print(f"{name} Serial No is  {index + 1}")
else:
    print(f"{name} is not in the list")