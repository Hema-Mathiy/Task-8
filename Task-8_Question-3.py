class Circle:
    _pi = 3.141

    def __init__(self, radii):
        self.radii = radii

    @classmethod
    def area(cls, radius):
        return cls._pi * radius ** 2

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls._pi * radius

    @classmethod
    def calculate_properties(cls, radii):
        results = []
        for radius in radii:
            area = cls.area(radius)
            perimeter = cls.perimeter(radius)
            results.append((radius, area, perimeter))
        return results


# Create an instance of the Circle class with the provided list of radii
data_list = [10, 507, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(data_list)

# Calculate and print the area and circumference for each circle in the list
circle_properties = Circle.calculate_properties(data_list)

for i, (radius, area, perimeter) in enumerate(circle_properties):
    print(f"Circle {i + 1}:")
    print(f"Radius: {radius}")
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
    print()
