def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()
