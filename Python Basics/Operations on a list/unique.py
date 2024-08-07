my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
unique_list = []
# Write your code here.
for i in range(len(my_list)-1):
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)

