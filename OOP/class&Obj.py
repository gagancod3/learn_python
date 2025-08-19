# name of class should be capitalized

# class
class Car:
    # methods
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f'{self.brand} {self.model}'

    def fuel_type(self):
        return "Petrol"

my_car = Car("Toyota","Innova") # Object
print(my_car.brand)

print(my_car.full_name()) 
print(my_car.fuel_type()) # Petrol



# inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # inheriting from parent class 
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electricity"
    
my_tesla = ElectricCar("Tesla", "Model Y", "90kWh")

print(my_tesla.model)
print(my_tesla.full_name())

# Polymorphism #
print(my_tesla.fuel_type()) # same fuel_type is in car class itself

# encapsulation #

class Bike:
    # methods
    def __init__(self, brand, model):
    # '__' prefix in attribute name is used to declare 'private' attribute
    #  won't be available in Objects directly
        self.__brand = brand 
        self.model = model

    # convention is to use prefix 'get' for a getter method
    def get_brand(self):
        return f"Brand: {self.__brand}"

    def full_name(self):
        return f'{self.__brand} {self.model}'

    def fuel_type(self):
        return "Petrol"
# I've added a getter method get_brand in class

my_bike = Bike("Yamaha","R15") # Object
# print(my_bike.__brand)

print(my_bike.get_brand())
print(my_bike.full_name()) 

# setter method


# Class Variable

