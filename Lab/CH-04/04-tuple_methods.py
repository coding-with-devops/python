z = ( "Ashutosh", 7, 23, 5.8, True, "Aarvi", 1987,7, 'Rocky')
print(z)

count = z.count(7) # count the number of times 7 appears in the tuple
index = z.index(7) # returns the index of the first occurrence of 7 in the tuple
print(count)
print(index)

a = (1, 2, 3)
b = (3, 4, 5)
print(a + b)  # Output: (1, 2, 3, 4)
print(a * 3)  # Output: (1, 2, 3, 1, 2, 3)
print( 2 in a)  
print( 4 in a)  
for i in z:
    print(i)  # Output: 1 2 3