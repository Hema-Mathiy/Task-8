class Circle:
    _pi = 3.141  # Private class variable for pi

    def __init__(self, radius_list):
        self.radius_list = radius_list

    def calculate_area(self):
        areas = [Circle._pi * r ** 2 for r in self.radius_list]  # pi using in the class variable
        return areas

    def calculate_circumference(self):
        circumferences = [2 * Circle._pi * r for r in self.radius_list]  # pi using in the class variable
        return circumferences


# Create an instance of the Circle class with the provided list of radii
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
