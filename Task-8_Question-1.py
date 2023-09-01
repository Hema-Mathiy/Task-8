import math

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list   #initializing an instance of the Circle

    def calculate_area(self):
        areas = [math.pi * r ** 2 for r in self.radius_list]   #calculating the area of Circle
        return areas

    def calculate_circumference(self):
        circumferences = [2 * math.pi * r for r in self.radius_list]    #calculating the circumference of Circle
        return circumferences

# Create an instance of the Circle class
data_list = [10, 507, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(data_list)

# Calculate and print the areas and circumferences of the circles
areas = circle_instance.calculate_area()
circumferences = circle_instance.calculate_circumference()

for i, radius in enumerate(data_list):
    print(f"Circle {i + 1}:")
    print(f"Radius: {radius}")
    print(f"Area: {areas[i]}")
    print(f"Circumference: {circumferences[i]}")
    print()
