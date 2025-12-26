#  Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.


class Car:
    def __init__(self, brand, model):   # constructor
        self.__brand = brand
        self.model = model
        
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
# print(my_tesla.get_brand())

print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())


