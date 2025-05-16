import random

genres = {
    "rock": [
        "Highway to Thunder", "Stone Edge", "Electric Horizon", "Broken Strings", "Firestorm"
    ],
    "pop": [
        "Dance Tonight", "Glitter Star", "Heartbeat Beat", "City Lights", "Bubblegum Dreams", "Golden Echo"
    ],
    "jazz": [
        "Smooth Moods", "Blue Sax", "Autumn Swing", "Velvet Lounge", "Evening Brew"
    ],
    "classical": [
        "Moonlight Sonata", "Four Seasons", "Canon in D", "Nocturne Op.9", "The Swan"
    ],
    "hip hop": [
        "Street Flow", "Mic Drop", "Bassline King", "Urban Jungle", "Cipher Nights"
    ],
    "electronic": [
        "Neon Dreams", "Synth Pulse", "Cyber Drift", "Laser Rain", "Pixel Groove"
    ],
    "country": [
        "Dusty Roads", "Whiskey Moon", "Cowboy Heart", "Rodeo Wind", "Southern Lights"
    ],
    "reggae": [
        "Island Breeze", "Roots Vibe", "Jamaica Sun", "Peaceful Riddim", "Lion Spirit"
    ],
    "blues": [
        "Deep River Blues", "Midnight Slide", "Trainyard Soul", "Whiskey Strings", "Rusty Strings"
    ],
    "metal": [
        "Iron Skull", "Dark Inferno", "Chains of Wrath", "Echoes of Doom", "Blood Reign"
    ]
}


while True:
    aword = input("Enter which genre you like (or type 'exit' to quit): ").lower()
    if aword == 'exit':
        break
    elif aword not in genres:
        print("Sorry, don't know that genre.")
    else:
        print(f"Check out: {random.choice(genres[aword])}")
