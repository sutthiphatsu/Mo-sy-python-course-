"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle:
    def __init__(self,length,width):
        self.__legth=length
        self.__width=width
    def getArea(self):
        return f"{self.__width*self.__legth}"
    def getPerimter(self):
        return f"{self.__width*self.__legth*2}"
    def isSqar(self):
        return self.__width == self.__legth
find = Rectangle(7,9)
print(find.getArea())
print(find.getPerimter())
print(find.isSqar())
find2 = Rectangle(10,10)
print(find2.getArea())
print(find2.getPerimter())
print(find2.isSqar())
