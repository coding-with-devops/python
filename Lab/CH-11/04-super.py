class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal __init__ called. Name: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent constructor
        self.breed = breed
        print(f"Dog __init__ called. Breed: {self.breed}")

# Usage
d = Dog("Buddy", "Golden Retriever")
