class Rectangle:
    def __init__(self, color="default_color", is_filled=False, x_top_left=0, y_top_left=0, length=0, width=0):
        self.color = color
        self.is_filled = is_filled
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def __str__(self):
        return (f"Rectangle - Color: {self.color}, Filled: {self.is_filled}, "
                f"Top Left: ({self.x_top_left}, {self.y_top_left}), "
                f"Length: {self.length}, Width: {self.width}")

color = input("Enter color for the rectangle: ")
is_filled = input("Is the rectangle filled? (True/False): ").lower() == 'true'
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

user_rectangle = Rectangle(color=color, is_filled=is_filled, length=length, width=width)

print(user_rectangle)
