def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b
def thanks():
    return "Thank You"
    
# Dynamic function name and parameters
func_name = "greet"
params = ("Alice",)

# Call the function using globals()
result = globals()[func_name](*params)
print(result)  # Output: Hello, Alice!

# Another dynamic call
func_name = "add"
params = (10, 20)
result = globals()[func_name](*params)
print(result)  # Output: 30

func_name="thanks"
result = globals()[func_name]
print(result)