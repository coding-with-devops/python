name = "Ashutosh"
myname = "AshutoshMuduli"
description = '''This is a multi-line string.\n It can span multiple lines. \n It is useful for long text.'''

#emailid = input("Enter your email id: ")
# Len ()
print(len(name)) 
print(len("Muduli")) 
# startwith and endswith
print(name.startswith("A")) 
print(name.startswith("a")) 
print(name.endswith("h"))

print(myname.upper()) # Upper case
print(myname.lower()) # Lower case
print(myname.title()) # Title case
print(myname.capitalize()) # Capitalize first letter
print(myname.swapcase()) # Swap case
print(myname.replace("M", "DD")) # Replace A with a
if myname.startswith("A") and myname.endswith("i"):
    print("My Name is : ", myname[0:8] + " " + myname[8:])
else:
    print("Invalid name")
'''
if emailid.endswith("gmail.com"):
    print("Valid Email ID")
else:   
    print("Invalid Email ID")
'''
# Split and Join
print(myname.split("u")) # Split string into list
print(myname.split("M")) # Split string into list
print(myname.split()) # Split string into list
print("-----------------------------------")

print(description.find("line")) # Find first occurrence of u
print(description.count("line")) # Find first occurrence of u
print(description.rfind("line")) # Find last occurrence of u
print(description.index("line")) # Find first occurrence of u
print(description.replace("line", "bar")) # Replace first occurrence of u
print("-----------------------------------")
print(description)
print(myname.isalnum()) # Check if string is alphanumeric
print(myname.isalpha()) # Check if string is alphabetic
print(myname.isdigit()) # Check if string is digit
print(myname.islower()) # Check if string is lowercase 
print(myname.isupper()) # Check if string is uppercase
print(myname.isspace()) # Check if string is space
print(myname.isnumeric()) # Check if string is numeric