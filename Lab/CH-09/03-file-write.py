## write on a file

text_entry = "Today date is Nice Day"

file = open("my_file.txt", "w")
file.write(text_entry)
file.close()


with open('my_file1.txt', 'w') as file1:
    file1.write('Hello, world!')
    # You can log something meaningful instead of printing the file object
    print("File written successfully.")