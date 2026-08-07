def calculate_triangle_area(hight, long):
    """Calculates and displays rectangle area"""
    area = 1/2 * hight * long
    print(f"triangle with length {hight} and width {long}")
    print(f"Area = 1/2 x {hight} × {long} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)
height = float(input("Enter the height to calculate: "))
length = float(input("Enter the length to calculate: "))
calculate_triangle_area(height, length)