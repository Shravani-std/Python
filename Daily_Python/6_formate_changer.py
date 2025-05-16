word = str(input("Enter sentence: "))
formate_num = int(input(print("Enter formate number:" \
"1.UPPERCASE" \
"2.lowercase" \
"3.Title" \
"4.sentence case ")))

if formate_num == 1:
    print(word.upper())
elif formate_num == 2:
    print(word.lower())
elif formate_num == 3:
    print(word.title())
elif formate_num == 4:
    print(word.capitalize())
else:
    print("Formate not available")