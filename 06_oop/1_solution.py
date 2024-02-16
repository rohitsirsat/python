class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get__brand(self):
        return self.__brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod
    def car_description():
        return "stop using cars"
    
    @property
    def model(self):
        return self.__model



class ElectricCar(Car):
    def __init__(self , brand, model, battery_size):
        super().__init__(brand, model)
        self.battety_size = battery_size
    
    def fuel_type(self):
        return "Electric charge"


# print(Car.car_description())

# Car("Tata", "safari")
# Car("Tata","Nexon")

# print(Car.total_car)

# my_tesla = ElectricCar("Tesls", "Model S", "87kwh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.get__brand())
# print(my_tesla.full_name())

# safari = Car("Tata","Safari")
# print(safari.model)

# print(safari.fuel_type())
# print(my_tesla.fuel_type())


# my_car = Car("Toyoto","Corolla")
# print(my_car.brand)
# print(my_car.model)

# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")

# print(my_new_car.model)
    
class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())