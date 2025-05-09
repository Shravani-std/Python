import random

print("Flip coin")
print("Guess heads and tails")

coin = ["heads", "tails"]

while True:
    choose = input("Enetr H for heads and T Tails...").lower()
    
    if choose != "heads" and choose != "tails":
        print("Wrong Choice")
        continue

    flip = random.choice(coin)

    print(f"Coin fliped {flip}")
    if flip == choose:
        print("You won ")
        


