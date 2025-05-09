import random

print("SCRAMBLED WORD")

while True:
    word = input("Enter a word: ")
    if word.lower() == "quit":
        print("Goodbye")
        break

    new = list(word)
    random.shuffle(new)  # shuffle in-place
    scrambled = "".join(new)
    print(f"Scrambled word: {scrambled}")
