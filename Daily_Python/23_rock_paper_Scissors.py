import random 

def paper_won(x, y):
    if x == "Rock" and y == "Paper":
        print(f"{y} won")
    return y

def rock_won(x, y):
    if x == "Rock" and y == "Scissors":
        print(f"{x} won")
    return x

def scissor_won(x, y):
    if x == "Paper" and y == "Scissors":
        print(f"{y} won")
    return y

print(" === Rock-Paper-Scissors ===")

print("Rules: " \
"\n- Rock Crushes Scissors" \
"\n- Scissors cut papers" \
"\n- Paper covers Rock" \
"\n- First to win 3 rounds is the champion! ")

rounds = 3
score_user = 0
computer_score = 0
initial_round = 1

while score_user < 3 and computer_score < 3:
    print("\nMake Your choice: " \
    "\n1. Rock" \
    "\n2. Paper" \
    "\n3. Scissors")
    
    print(f"\n=== Round {initial_round} ===")
    user_input = input("Enter choice number: ").strip()

    if user_input not in ["1", "2", "3"]:
        print("Invalid choice")
        continue

    cmp_input = ["Rock", "Paper", "Scissors"]
    computer_input = random.choice(cmp_input)

    if user_input == "1":
        user_input = "Rock"
    elif user_input == "2":
        user_input = "Paper"
    elif user_input == "3":
        user_input = "Scissors"

    print(f"You chose: {user_input}")
    print(f"Computer chose: {computer_input}")

    if user_input == computer_input:
        print("It's a tie!")
    elif (user_input == "Rock" and computer_input == "Paper"):
        paper_won(user_input, computer_input)
        computer_score += 1
    elif (user_input == "Rock" and computer_input == "Scissors"):
        rock_won(user_input, computer_input)
        score_user += 1
    elif (user_input == "Paper" and computer_input == "Rock"):
        paper_won(computer_input, user_input)
        score_user += 1
    elif (user_input == "Paper" and computer_input == "Scissors"):
        scissor_won(user_input, computer_input)
        computer_score += 1
    elif (user_input == "Scissors" and computer_input == "Rock"):
        rock_won(computer_input, user_input)
        computer_score += 1
    elif (user_input == "Scissors" and computer_input == "Paper"):
        scissor_won(computer_input, user_input)
        score_user += 1

    print(f"Score: You {score_user} - Computer {computer_score}")
    initial_round += 1

if score_user == 3:
    print("\nYou are the Champion!")
else:
    print("\nComputer is the Champion!")



