class Car:

    total_car = 0

    def __init__(self, brand, model) :
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
    
    @property
    def get_brand(self):
        return self.__brand + " !"
    
    
    def full_name(self):
    
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Disel"
    

    @property
    def get_model(self):
        return self.__model + " Non Changeable"
    
    @staticmethod
    def general_des():
        return "General description"

class ElectricCar(Car):
    def __init__(self, brand, model, battory_size):
        super().__init__(brand,model)
        self.battory_size = battory_size

        super().full_name()
    
    def fuel_type(self):
        return "Electric Charge"
        


my_car = Car("Tata", "A")
print(my_car.general_des()) # Should not be happened 
print(Car.general_des())  

my_car.__model = "City"  #Should not be Happened
#Solution
print(my_car.get_model)