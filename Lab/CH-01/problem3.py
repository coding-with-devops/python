import os

directory = "/"

content = os.listdir(directory)

print("Content of the directory:")
for item in content:
    print(item) 
    