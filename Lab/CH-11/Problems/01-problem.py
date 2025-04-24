import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"


class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)  # Call Vector2D's constructor
        self.z = z

    def magnitude(self):
        # Override to include z component
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"


# 🧪 Example usage
v2 = Vector2D(3, 4)
print(v2)                    # Output: Vector2D(3, 4)
print(v2.magnitude())        # Output: 5.0

v3 = Vector3D(1, 2, 3)
print(v3)                    # Output: Vector3D(1, 2, 2)
print(v3.magnitude())        # Output: 3.0
