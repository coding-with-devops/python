class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        return f"{self.greeting}, {name}!"

# Create an instance
h = Greeter("Hello")

# Now call the object like a function
print(h("Alice"))  # Output: Hello, Alice!
print(h("Bob"))    # Output: Hello, Bob!


