# Break and Continue in Python
for i in range(1, 100):
    if i == 101:
        print("Found 10")
        break   # Exit from the loop
    print(i)
else:
    print("End of for loop")
####### Continue Statement
# The continue statement is used to skip the current iteration of a loop and move to the next iteration.
for j in range(1, 10):
    if j == 5:
        continue   #skip 
    print(j)
    print("End of for loop")

## Pass Statement
# The pass statement is a null operation; it does nothing when executed. It is often used as a placeholder in loops or functions where code will be added later.
for i in range(1, 10):
    pass   # do nothing
k = 1
if k == 5:
    pass   # do nothing
else:
    print(i)
    print("End of loop")
if k == 5:
    pass   # do nothing
for i in range(4):
    print("printing") 
    if i == 2: 
        continue 
    print(i)