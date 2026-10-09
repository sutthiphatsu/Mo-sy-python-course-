""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_info(self):
        return f"Vehicle info\nbrand:{self.brand}\nmodel:{self.model}\nyear:{self.year}"
class Car(Vehicle):
    def __init__(self,brand,model,year,number_of_doors,):
         super().__init__(brand,model,year)
         self.number_of_doors = number_of_doors
    def get_info(self):
         return f"Vehicle info\nbrand:{self.brand}\nmodel:{self.model}\nyear:{self.year}\nnumber of doors:{self.number_of_doors}"
car1 = Vehicle("apple","pieapple","1999")
print(car1.get_info())
print("\n")
car2 = Car("apple","pieapple","1999","8")
print(car2.get_info())


