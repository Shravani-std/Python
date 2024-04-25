rows = int(input("Enter the no. if rows: "))

for i in range(1, rows - 1):
    for j in range(1, rows - i + 1):
        print(end=' ')
    for star in range(1, i + 1):
        print("*",end=' ')
    print(' ')