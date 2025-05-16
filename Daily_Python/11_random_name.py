import random
first_names = [
    "Olivia", "Liam", "Ava", "Noah", "Sophia",
    "Mason", "Isabella", "Ethan", "Mia", "Lucas",
    "Harper", "Logan", "Amelia", "James", "Ella",
    "Benjamin", "Chloe", "Henry", "Aria", "Jack"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin"
]
cnt = int(input("How many named u wanna generate: "))

for i in range(cnt):
    full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    print(full_name)


