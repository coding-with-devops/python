class Number:
    def __init__(self, value):
        self.value = value
        print(f" 1st NO: {self.value}")

    def __add__(self, other):
        return (self.value + other.value)

a = Number(10)
b = Number(20)
print(a + b)  # Output: 30
