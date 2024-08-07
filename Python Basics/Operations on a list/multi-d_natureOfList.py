temps = [[0.0 for h in range(24)] for d in range(31)]
total = 0.0
for day in temps:
    total += day[11]

average = total / 31
print("Average temperature at noon:", average)


#ex.2
temp = [[0.0 for t in range(24)] for f in range(31)]
high = -100.0
for day in temp:
    for temp in day:
        if high < temp:
            high = temp
print("Higher Temperatur : ",high)


#ex.3
temps = [[0.0 for h in range(24)] for d in range(31)]
hot_days = int(input("Enter the number of days: "))
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
print(hot_days, "days were hot.")

rooms = [[[0 for r in range(10)] for f in range(10)] for t in range(2)]
print(rooms)