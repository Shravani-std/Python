import time

print("Count down from chosen seconds!")


while True:
    secs = int(input("Enter seconds to countdown from: "))
    print(f"Starting count from {secs} seconds")
    
    if secs <= 0:
        print("Not valid number")
    for i in range(secs,0,-1):
        print(f"{i} seconds remaining...")
        time.sleep(1)

    print("\n Countdown has been completed")
    again = input("Want to do next counter? (y/n) ")
    if not again.startswith("y"):
        print("Done")
        break