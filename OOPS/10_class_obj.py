import sys

class Hero:
    def __init__(self, health, level):
        self._health = health
        self.level = level
    
    # To access private member we use getter and setter 
    def get_health(self):
        return self._health + " + "
    
    def set_health(self, h):
        self._health = h

h1 = Hero("Good", 12)
print(f"Health: {h1._health} + Level: {h1.level}")
h1._health = "Bad"
h1.level = 80
print(f"Health: {h1._health} + Level: {h1.level}")

print(h1.get_health())
print(h1.set_health("Critical"))
print(h1.get_health())

# a = [1, 2, 3]
# b = 10
# print(id(b))  # Address in heap memory
