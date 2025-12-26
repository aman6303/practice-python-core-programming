# Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand, model):   # constructor
        self.__brand = brand
        self.model = model
        
    def get_brand(self):                # always write the getter method name with get
        return self.__brand + "!"
        
    def full_name(self):               # creating a method
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.__brand)  # we cannot access directly
print(my_tesla.get_brand())

# similary we can set the value using setter methods