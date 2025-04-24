#

with open("poems.txt", "r") as file:
   content = file.read()
if "twinkle" in content:
    print(f"  word is present")
else:
     print(f" word is not present") 

    