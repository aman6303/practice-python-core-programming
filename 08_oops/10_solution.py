# Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.


class Car:
    total_car = 0  # track no of object created
    
    def __init__(self, brand, model):   # constructor
        self.__brand = brand
        self.__model = model
        Car.total_car +=1  # we can do it using self also
        
    def get_brand(self):                # always write the getter function name with get
        return self.__brand + "!"
        
    def full_name(self):               # creating a method
        return f"{self.brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    
    
class Battery:
    def batter_info(self):
        return "This is Battery"

class Engine:
    def engine_info(self):
        return "This is Engine"
    
class ElectricCar(Battery, Engine, Car):                # Multiple inheritance
    pass
    
my_new_tesla = ElectricCar("Tesla", "Model S")
print(my_new_tesla.batter_info())
print(my_new_tesla.engine_info())