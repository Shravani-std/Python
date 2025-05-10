import random
print("Guess Number from (1-15) you've 10 chances ")

chances = 10

# numbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']


guess = input("\nEnter number: ")
playing = True
while playing:
    random_num = random.randint(1,100)
    attempt = 0
    max_attempts = 10

    game_over = False

    while attempt < max_attempts and not game_over:
        try:
            guess = int(input(f"Attempt {attempt+1}/{max_attempts}.Enter Your guess: "))

        except ValueError:
            print("Please enter valid number ")
            continue

        attempt += 1
        if guess < random_num:
            print("too low try higher!")
        elif guess > random_num:
            print("try lower")
        else:
            print("You won")
            game_over=True

        
