goal = int(input("Enter Goal steps: "))
reach = int(input("Enter reached steps: "))




if goal > reach:
    target = goal - reach
    print(f"You have to complete {target} stpes yet.")
elif reach > goal:
    extra = reach-goal
    print(f"You have completed {extra} stpes extra good")