word = input("Enter character: ")

if  word.isalpha():
    print("This is a character")
elif word.isdigit():
    print("This is a number")
else:
    print("Speacial CHaracter")