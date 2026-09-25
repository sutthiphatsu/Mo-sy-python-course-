"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area
    def get_area(self):
        area = self.length * self.width
        return f"ที่คืนค่าพื้นที่ของสี่เหลี่ยม:{area}"

    # Method to get the perimeter
    def get_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return f"ที่คืนค่ารอบรูปของสี่เหลี่ยม:{perimeter}"


rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30

class Circel:
    def __init__(self, radius,):
        self.radius = radius
        self.pai = 3.14159

    # Method to get the area
    def get_area(self):
        area_Circel = self.pai *self.radius**2
        return f"ที่คืนค่าพื้นที่ของวงกลม:{area_Circel}"

    # Method to get the perimeter
    def get_perimeter(self):
        perimeter = 2 * (self.pai * self.radius)
        return f"ที่คืนค่ารอบรูปของวงกลม:{perimeter}"
my_circle = Circel(5)
print(my_circle.get_area())       
print(my_circle.get_perimeter())