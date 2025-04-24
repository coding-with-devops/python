with ( 
    open('file1.txt') as f1, 
    open('file2.txt') as f2 ):
    c1 = f1.read()
    c2 = f2.read()

print(c1, " ", c2)