# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0]) 
print(my_tuple[1:4])


# Creating a tuple with different data types
mixed_tuple = (1, "hello", 3.14, [1, 2, 3])
print(mixed_tuple[1]) 
print(mixed_tuple[3]) 


# Creating a tuple with nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0])  
print(nested_tuple[1][0]) 



# Creating a tuple with a single element
single_element_tuple = (42,)
print(single_element_tuple[0])
data = (10, 20, 30, 40, 50)
slice1 = data[1:4]
slice2 = data[:3]
slice3 = data[2:]
print("Slice 1:", slice1)
print("Slice 2:", slice2) 
print("Slice 3:", slice3) 
