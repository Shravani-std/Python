class Car:

    total_car = 0

    def __init__(self, brand, model) :
        self.__brand = brand
        self.model = model
        Car.total_car += 1
    
    @property
    def get_brand(self):
        return self.__brand + " !"
    
    # # @__brand.setter
    # def set_NewBrand(self, newBrand):
    #     self.__brand = newBrand
    
    def full_name(self):
    
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Disel"

class ElectricCar(Car):
    def __init__(self, brand, model, battory_size):
        super().__init__(brand,model)
        self.battory_size = battory_size

        super().full_name()
    
    def fuel_type(self):
        return "Electric Charge"
        

tesla  = ElectricCar("Tesla", "Model s", "85kw")
print(tesla.model)
# print(tesla.__brand)

print(tesla.full_name())
print("Tesla Fuel Type:",tesla.fuel_type())

tata =   Car("Tata","A")
safari = Car( "Safari","B")
toyota = Car("Toyota","C")
print("safari Fuel Type:",safari.fuel_type())

print("No. of cars od objects initialized in Car class+from its inherited class: ",Car.total_car)




# Poly == Same method but access different output
# total_car == accessed by both saem class and inherited class by using polymorphism
                   #total_car comes next satic methods