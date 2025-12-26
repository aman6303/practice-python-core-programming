# Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.


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
    
class ElectricCar(Car):                # inheritance
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"
    
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

safari = Car("Tata", "Safari")

# safari.model = "City"  # changing the varibale

print(safari.model)