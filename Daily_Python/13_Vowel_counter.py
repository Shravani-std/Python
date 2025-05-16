print("Vowel_counter")

vv = ["a","e","i","o","u"]
while True:
    word = input("Enter a word: ")
    if word.lower() == "quit":
        print("End")
        break

    vowel_cnt = 0

    for letter in word:
        if letter in vv:
            vowel_cnt+=1

    print(vowel_cnt)
    


