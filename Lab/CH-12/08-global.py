a = 10
def show():
    global a 
    a = 50
    return a

print(a)
print(show())
print(a)
