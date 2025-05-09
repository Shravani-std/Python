import random

proteins = ["chicken", "tofu", "paneer", "beef", "shrimp"]
vegetables = ["broccoli", "spinach", "carrot", "bell pepper", "zucchini"]
carbs = ["rice", "pasta", "noodles", "bread", "quinoa"]
spices = ["garlic", "ginger", "turmeric", "paprika", "cumin"]
sauces = ["soy sauce", "tomato sauce", "alfredo", "pesto", "schezwan"]


def random_recipe():
    protein = random.choice(proteins)
    vegetable = random.choice(vegetables)
    carb = random.choice(carbs)
    spice = random.choice(spices)
    sauce = random.choice(sauces)


    recipe = f"""
    1. Cook some {carb} as your base.
    2. In a pan, sauté {spice} and add {protein}.
    3. Add chopped {vegetable} and cook till tender.
    4. Pour in some {sauce} and mix well.
    5. Serve hot over {carb} and enjoy!
    """


    return recipe


print(random_recipe())