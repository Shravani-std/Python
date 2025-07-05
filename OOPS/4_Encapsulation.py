class Car:
    def __init__(self, brand, model) :
        self.__brand = brand
        self.model = model
    
    def get_brand(self):
        return self.__brand + " !"
    
    def set_NewBrand(self, newBrand):
        self.__brand = newBrand
    
    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battory_size):
        super().__init__(brand,model)
        self.battory_size = battory_size

        super().full_name()
        

# _brand not accessed by other class coz of encapsulation of _brand member 
# tesla  = ElectricCar("Tesla", "Model s", "85kw")
# print(tesla.model)
# print(tesla.__brand)

# print(tesla.full_name())



##Accessible private
car = Car("Mahindra","A")
print(car.get_brand())

car.__brand = "Tata"
print("New Brand setted using setter method securly privately: ",car.__brand)






#__brand == Making it private cannot accessed by other classes objects but we can access attributes using same class objects