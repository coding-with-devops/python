#   problem 1
#Write a program to store seven fruits in a list entered by the user.
fruits = []
#for i in range(7):
for i in range(1,8):
    fruit = input(f"Enter fruit name {i}: ")
    fruits.append(fruit)  
print("The fruits are:" + str(fruits))  
for fruit in fruits:
    print(fruit)