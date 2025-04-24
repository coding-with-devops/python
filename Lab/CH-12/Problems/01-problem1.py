try:
    with ( open("file1.txt", "r") as f1, 
           open("file2.txt", "r") as f2,
           open("file3.txt", "r") as f3,
          ):
        file1 = f1.read()
        file2 = f2.read()
        file3 = f3.read()
    print(file1,file2,file3)
except FileNotFoundError as e:
    print("any of these files are not present")

