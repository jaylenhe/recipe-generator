from conversation_words import *
from pick_and_filter import *
import re

# main file to run

def main():

    greeting = "Hello! Welcome to the Dinn-o-matic! What you like to select something to eat?" + ye_nay
    yes_no = int(input((greeting)))
    
    while True:
        if yes_no == 1:
            time_to_cook = input("Great! How much time do you have to cook today? Ex: 10 minutes, 1 hour \n")
            
            if int(re.search(r"\d+", time_to_cook).group(0)) <= 0:
                print("No time for a recipe today.")
                break
            else:
                ingredients_available = input("Ok! What ingredient(s) do you have right now? (Separate by commas): ")
                ingredients_available = [ingredient.strip() for ingredient in ingredients_available.split(",")]

                num = re.search(r"\d+", time_to_cook).group(0)
                time = re.search(r"[a-zA-Z]+", time_to_cook).group(0)

                print("Now generating a recipe...")
                
                # pick a random recipe that meets the time and ingredient constraints
                recipes = filtered_recipes(num, time, ingredients_available)
                if recipes:
                    pick(recipes)
                else:
                    print("No recipes with given time and ingredients")
                break

        elif yes_no == 2:
            print(goodbye)
            break
        else:
            yes_no = int(input(error))

if __name__ == "__main__":
    main()
