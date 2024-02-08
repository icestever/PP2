class MyShape:
    def __init__(self, color="default_color", is_filled=False):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"MyShape - Color: {self.color}, Filled: {self.is_filled}"

    def get_area(self):
        return 0



my_shape = MyShape()
print(my_shape)  # Output: MyShape - Color: default_color, Filled: False
print("Area:", my_shape.get_area())  # Output: Area: 0
