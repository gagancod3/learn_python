# name of class should be capitalized

# Class
class Car:

    # Class Variable # common to all objects
    total_car = 0 
    
    # Methods
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model # private attribute
        # incrementing class variable
        Car.total_car += 1

    def full_name(self):
        return f'{self.brand} {self.__model}'

    def fuel_type(self):
        return "Petrol or Diesel"
    
    # static method # 
    # here we don't need to use self or class variable
    @staticmethod
    def general_info():
        return "Cars are used for transportation"

    @property # getter method for private attribute***
    def model(self):
        return self.__model
    
# Object 
my_car = Car("Toyota","Innova") 

print(my_car.brand) # Toyota
# print(my_car.__model) # can't access private attribute directly
print(my_car.full_name()) # Toyota Innova
print(my_car.fuel_type()) # Petrol


# trying to update private attribute
# my_car.model = "Fortuner" # AttributeError: property 'model' of 'Car' has no setter

# accessing private attribute using property decorator
print(my_car.model) # Innova 

print(my_car.__dict__) # {'brand': 'Toyota', '_Car__model': 'Innova', 'model': 'Fortuner'}

# trying to access static method
print(Car.general_info()) 

# Inheritance #
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # inheriting from parent class 
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electricity"
    
my_tesla = ElectricCar("Tesla", "Model Y", "90kWh")

# print(my_tesla.model) # can't access private attribute of parent class
print(my_tesla.battery_size)
print(my_tesla.full_name())

# Polymorphism #
print(my_tesla.fuel_type()) # same fuel_type is in car class itself

safari = Car("Tata", "Safari")

# accessing class variable
print(Car.total_car) # 3

# 3 objects created so far
'''
my_car = Car("Toyota", "Innova")
my_tesla = ElectricCar("Tesla", "Model Y", "90kWh") - inherited from Car class
safari = Car("Tata", "Safari")
'''


# validating my_tesla object is from ElectricCar class and Car class

# SYNTAX: isinstance(object, class) 

print(isinstance(my_tesla, ElectricCar)) # True
print(isinstance(my_tesla, Car)) # True

# Encapsulation #

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
    

my_bike = Bike("Yamaha","R15") # Object

# print(my_bike.__brand) # not accessible since it's private

print(my_bike.get_brand())
print(my_bike.full_name()) 


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

    def battery_info(self):
        return f"Battery capacity is {self.capacity} kWh"

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def engine_info(self):
        return f"Engine horsepower is {self.horsepower} HP"
    
# Multiple Inheritance #
# order of inheritance matters # (left to right, depth first) 
class HybridCar(Battery, Engine, Car):
    def __init__(self, brand, model, capacity, horsepower):
        Car.__init__(self, brand, model) # initializing Car class
        Battery.__init__(self, capacity) # initializing Battery class
        Engine.__init__(self, horsepower) # initializing Engine class


my_hybrid = HybridCar("Toyota", "Prius", 8.8, 121)

print(my_hybrid.full_name()) # from Car class # Toyota Prius
print(my_hybrid.battery_info()) # from Battery class # Battery capacity is 8.8 kWh
print(my_hybrid.engine_info()) # from Engine class # Engine horsepower is 121 HP