# For loop
'''
for i in range(15):
    print(i + 1 , end=", ")
rows = 5
'''
i = 1
for i in range(1, 6):
    #print( "*")
    for j in range(1, i + 1):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*")