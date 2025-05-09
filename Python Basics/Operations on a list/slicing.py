# negative indices to perform slices
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)

#ex.2
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]
 
print(slice_one)  
print(slice_two)  
print(slice_three) 


#ex.3
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  
 
del my_list[:]
print(my_list) 



#ex.3
my_list = ["A", "B", 1, 2]
 
print("A" in my_list) 
print("C" not in my_list) 
print(2 not in my_list)



