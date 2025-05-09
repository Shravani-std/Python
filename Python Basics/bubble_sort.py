my_list=[]
swapped = True
n = int(input("Enter The number of elements:"))

print("Enter elements: ")
for i in range(n):

    ele = int(input())
    my_list.append(ele)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i+1]:
            swapped = True
            my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
print("Sorted List is: ")
print(my_list)


# num = [2,7,1,9,10,4,6]
# swapped = True

# while swapped:
#     swapped = False
#     for i in range(len(num) - 1):
#         if num[i] > num[i+1]:
#             swapped = True
#             num[i],num[i+1] = num[i+1],num[i]
# print(num)

