
file_names = ["file1.txt", "file2.txt", "file3.txt"]

for file in file_names:
    try:
        with open(file, "r") as file:
            content = file.read()
            #print(f"--- Contents of {file} ---")
            print(content)
    except FileNotFoundError:
        print(f"{file} not found.")

