import random
from collections import Counter
someWords ='''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''


someWords = someWords.split(' ')
word = random.choice(someWords)

# inp = input("Enter a word: ")
if __name__ ==  '__main__':
    print("Guess Word in Fruit...")

    for a in word:
        print('_', end='')
    print()

    storeWord = ''
    chances = len(word) + 2
    flag = 0
    correct = 0

    try:
        while (chances!= 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input("Enter guess Word: "))
            except:
                print("Enter only a letter!")
                continue

            # validation guess
            if not guess.isalpha():
                print("Enter only a LETTER")
                continue
            elif len(guess) > 1:
                print("Enter inly a Simple LETTER.")
                continue
            elif guess in storeWord:
                print("You have already guessed that number. ")


            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    storeWord += guess

            for char in word:
                if char in storeWord and (Counter(storeWord) != Counter(word)):
                    print(char, end=" ")
                    correct += 1

                elif (Counter(storeWord) == Counter(word)):
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print("Guessed right...!")
                    break
                    break
                else:
                    print('_', end=' ')

        if chances <= 0 and (Counter(storeWord) != Counter(word)):
            print()
            print("You losttry again")
            print("The word was {}".format(word))


    except KeyboardInterrupt:
        print()
        print("Try Again!")
        exit()
