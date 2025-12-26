# Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

# static method is the method that belongs to class rather than an instance of a class

class Car:
    total_car = 0  # track no of object created
    
    def __init__(self, brand, model):   # constructor
        self.__brand = brand
        self.model = model
        Car.total_car +=1  # we can do it using self also
        
    def get_brand(self):                # always write the getter function name with get
        return self.__brand + "!"
        
    def full_name(self):               # creating a method
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
class ElectricCar(Car):                # inheritance
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"
    
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.general_description())

safari = Car("Tata", "Safari")
# print(safari.general_description())

print(Car.total_car) 
print(Car.general_description())

