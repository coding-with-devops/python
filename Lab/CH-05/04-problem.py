#Create an empty dictionary. 
# #Allow 4 friends to enter their favorite language as value and use key as their names. 
# Assume that the names are unique.
dict = {}
languages = []
names = []
for i in range(4):
   names = input("Enter your name: ")
   languages = input(f"Enter {names}'s favorite language: ")
   dict.update({names: languages})
print(dict)