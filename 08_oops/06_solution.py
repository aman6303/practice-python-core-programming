# Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

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
    
class ElectricCar(Car):                # inheritance
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"
    
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.__brand)  # we cannot access directly
print(my_tesla.get_brand())
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())
# print(safari.total_car)   # accessig the variable of class (not the correct way)

print(Car.total_car)  # this is the correct way of accessing class variable

# sometime python store some variables even after cleaning for optimizarion purpose
# its not an logical error - just restart the terminal/kernal

