import math

class MyShape:
    def __init__(self, color="default_color", is_filled=False):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"MyShape - Color: {self.color}, Filled: {self.is_filled}"

    def get_area(self):
        return 0

class Rectangle(MyShape):
    def __init__(self, color="default_color", is_filled=False, x_top_left=0, y_top_left=0, length=0, width=0):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def __str__(self):
        return (f"Rectangle - Color: {self.color}, Filled: {self.is_filled}, "
                f"Top Left: ({self.x_top_left}, {self.y_top_left}), "
                f"Length: {self.length}, Width: {self.width}")

    def get_area(self):
        return self.length * self.width

class Circle(MyShape):
    def __init__(self, color="default_color", is_filled=False, x_center=0, y_center=0, radius=0):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def __str__(self):
        return (f"Circle - Color: {self.color}, Filled: {self.is_filled}, "
                f"Center: ({self.x_center}, {self.y_center}), Radius: {self.radius}")

    def get_area(self):
        return math.pi * self.radius**2
#ex
rectangle = Rectangle(color="blue", length=5, width=3)
print(rectangle)
print("Area:", rectangle.get_area())

circle = Circle(color="red", radius=4)
print(circle)
print("Area:", circle.get_area())
