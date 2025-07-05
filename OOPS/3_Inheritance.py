class Car:
    def __init__(self, brand, model) :
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battory_size):
        super().__init__(brand,model)
        self.battory_size = battory_size

        super().full_name()
        

tesla  = ElectricCar("Tesla", "Model s", "85kw")
print(tesla.model)

print(tesla.full_name())
