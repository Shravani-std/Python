import random
import time
print("Respond with related word quickly!")

words = {
    "Tree": ["leaf", "root", "branches", "flowers", "fruits"],
    "Car": ["engine", "wheels", "doors", "seats", "steering"],
    "Computer": ["keyboard", "mouse", "monitor", "CPU", "RAM"],
    "House": ["roof", "walls", "windows", "doors", "floor"],
    "Human": ["head", "arms", "legs", "heart", "brain"],
    "Book": ["cover", "pages", "spine", "title", "chapters"],
    "Phone": ["screen", "battery", "camera", "buttons", "speaker"],
    "Bird": ["wings", "beak", "feathers", "legs", "tail"],
    "Bike": ["handle", "pedal", "wheel", "seat", "brake"],
    "Flower": ["petals", "stem", "leaves", "pollen", "roots"]
}
score=0
rounds =0
while True:

    random_word = random.choice(list(words.keys()))
    related_word = words[random_word]
    print(f"Prompt Word: {random_word.upper()}")
    guess = str(input("Quickly type a word related to this prompt!"))
    timme = time.time()
    response = input("> ").lower().strip()

    response_time =  time.time() - timme
    if response in related_word:
        points = max(1,5 - int(response_time))
        score += points


        print(f"Good Association! +{points} points (answered in {response_time}s) ")
    else:
        print("Not common guess")

        rounds +=1
     
    if input("Wanna play again? (y/n) ").lower().startswith('n'):
        print("Bye")
        break

