class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def radius(self):
        """Getter for radius"""
        return self._radius
    @radius.setter
    def radius(self, value):
        """Setter for radius with validation"""
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value
    @property
    def area(self):
        """Read-only property (no setter)"""
        return 3.14159 * self._radius ** 2
    
c = Circle(5)
print(c.radius)       
print(c.area)

c = Circle(10)
print(c._radius)
print(c.area)


