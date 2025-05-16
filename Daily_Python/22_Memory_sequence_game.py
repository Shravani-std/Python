import random
import time
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")





print("=== Memory Sequence Game ===")

print("Rules: " \
"\n- Watch as numbers appear one by one" \
"\n- After the sequence is shown, type it back in order" \
"\n- Each round adds one more number to rememmber" \
"\n- How far can you go?")

print("Press Enter to start...")

sequence = []
current_round = 1
game_over = False
while not game_over:
    print(f"\n=== Round - {current_round} ===")

    print(f"Remember this sequence of nums {len(sequence)} numbers:  ")
    sequence.append(random.randint(1,9))
    clear_screen()
    #game start
    
    for num in sequence:
        time.sleep(0.7)
        print(f"{num}")
        time.sleep(0.7)
        clear_screen()

    print("\n Now repeat the sequence by typing each number, seperated by spaces ")
    player_answer = input("> ")


    try:
        player_sequnece = [int(num1) for num1 in player_answer.split()]
    except ValueError:
        print(" Please enter numbes only!")
        game_over = True
        continue

    if player_sequnece == sequence:
        print(f"You won remembered {len(sequence)} numbers! ")
        current_round += 1
        time.sleep(2)
    else:
        print(f" Game over! You rememberd all {current_round-1} numbers!")

        print(
            f"The correct sequence was: {' '.join(str(num1) for num1 in sequence)}")
        game_over = True

    if game_over:
        play_again = input("\n Play again? (y/n): ").lower()
        if play_again.startswith("y"):
            sequence = []
            current_round = 1
            game_over = False
        else:
            print("Thanks for Playing")
