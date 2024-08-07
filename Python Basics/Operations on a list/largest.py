my_list = [10, 8, 6, 41, 2]
largest = my_list[0]
for i in range(len(my_list)-1):
    if largest < my_list[i]:
        largest = my_list[i]
print(largest)