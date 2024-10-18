# Creating a set
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")


fruits.remove("banana")

print("apple" in fruits)  
print("banana" in fruits)

print(fruits) 


# Creating a set with mixed data types
mixed_set = {1, "hello", 3.14, (1, 2, 3)}
print(mixed_set) 



# Creating a set of squares of numbers from 0 to 4
squares = {x**2 for x in range(5)}
print(squares) 



# Creating a set
colors = {"red", "green", "blue"}
colors.add("yellow")
colors.discard("green") 
colors.clear()
print(colors) 
