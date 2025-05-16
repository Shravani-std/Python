import random

a = int(input("Enter Lower number: "))
b = int(input("Enter Higher number: "))

range_range = random.randrange(100)

print("Now Guess random number: ")
chances = 5
guess_counter = 0

while guess_counter< chances:

    print("Enter guess Number: ")
    c = int(input())
    guess_counter += 1
    if c == range_range:
        print("You've guessed right number...")
    elif guess_counter >= chances and c != range_range:
        print(f'Oops sorry, The number is {range_range} better luck next time')

    elif c > range_range:
        print('Your guess is higher ')

    elif c < range_range:
        print('Your guess is lesser')


if guess_counter == chances:
    print("Your guesses are finished... ")