#A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

list1 = [ str(i*7) for i in range(1,11)]

print(list1)

new = "\n".join(list1)

print(new)