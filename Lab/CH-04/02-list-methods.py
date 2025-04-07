items = [ "apple", "banana", 22, 45.09, False, 62 , True, "cherry" ]
print(items)
items.append("orange") # add an item to the end of the list
print(items)

lsit1 = [1, 22, 3 ,66, 54, 99, 12, 0, 45, 78, 23, 11]
lsit1.sort() # sort the list in ascending order
print(lsit1)
lsit1.insert(7, 100) # insert 100 at index 0
print(lsit1)
lsit1.remove(12) # remove 100 from the list
print(lsit1)
value = lsit1.pop(5) # remove the first item from the list
print(lsit1)
print(value)
print(type(lsit1)) # check the type of the list
print(type(items)) # check the type of the list
a = "hello" # create a string variable
print(type(a)) # check the type of the variable