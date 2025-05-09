
scores = []

while True:
    score = input("Enter ur Makrs (or 'done'): ")
    if score.lower() == 'done':
        print("Good bye")
        break

    scores.append(float(score))
    average = sum(scores) / len(scores)
    print(f"Average score: {average: .2f}")

    if average >= 90:
        print("Grade: A")
    elif average <= 80:
        print("Grade: B")
    elif average <= 70:
        print("Grade: C")
    else:
        print("Grade: D & E")