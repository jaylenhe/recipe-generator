from conversation_words import *
import random, re
from scraped_data import aggregation


# choose a random recipe and update 'last made' if selected

def pick(generated_recipe):

    num_recipes = (len(generated_recipe) - 1)
    choice = iter(generated_recipe)

    while True:

        try:
            print(next(choice))

        except StopIteration:
            print("No more recipes!")
            break 

        print(" ")
        print(f"{num_recipes} recipes left!")
        print(" ")

        option = int(input(random.choice(inquiries) + ye_nay))
        num_recipes -= 1

        if option == 1:
            print("Great choice! Enjoy your meal!")
            print(' ')
            break
        elif option == 2:
            option2 = int(input("Would you like to select another meal?" + ye_nay))
            if option2 == 1:
                continue
            elif option == 2:
                print(goodbye)
                break
            else:
                print(error)
        else:
            option = int(input(error))

# filter recipe based on user input of time and ingredient constraints

def filtered_recipes(input_num, input_time, input_ingredients):

    filtered_recipes = []

    for recipe in aggregation():
        time_to_cook = recipe["Time to Cook"]
        num = int(re.search(r"\d+", time_to_cook).group(0))
        time = re.search(r"[a-zA-Z]+", time_to_cook).group(0)

        # Check time condition
        if (input_time == 'hour' and 'min' in time_to_cook and 'hour' not in time) or (num <= int(input_num) and input_time in time):
            # Check ingredients condition
            if all(any(item in ingredient for ingredient in recipe["Ingredients"]) for item in input_ingredients):
                filtered_recipes.append(recipe)

    return filtered_recipes

  
