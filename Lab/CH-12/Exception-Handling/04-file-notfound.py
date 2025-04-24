try:
    with open("file3.txt", "r") as f:
        file = f.read()
    print(file)
except FileNotFoundError as e:
    print(e)

print("Thanks")