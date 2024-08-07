my_list = [2,6,8,9,45,6,11,8,0,43,55,86,3]
find = 8
found = False


for i in range(len(my_list)):

    found = my_list[i] == find
    if found:
        break
if found:
    print("Found no. at",i,"th index")
else:
    print("Not found")