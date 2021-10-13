from ascii_art import *

transportations = ["Bicycle", "Bus", "Taxi"]
collected_items = []
items_in_store = ["Banana","Sugar","Cornstarch","Baking-Soda","Whipped-Cream","Flour","Chocolate","Butter","Milk","Salt"]
required_ingredients = ["Strawberries","Sugar","Cornstarch","Whipped-Cream","Flour","Butter","Salt"]
display_required_items = "|Strawberries| |Sugar| |Cornstarch| |Whipped-Cream| |Flour| |Butter| |Salt|"

def trap_room():
    print("You lost the game")
    return False

def home():
    print(display_home)
    print("I have collected:", collected_items)
    print("'All the required ingredients are ready to be baked into a YUMMY strawberry fruit pie.'")
    print("Thank you for helping me out to bake a most delicious strawberry fruit pie in the world!")
    print("You won the game!")

def select_transportation():
    print("\n- Please type: Bicycle, Bus, or Taxi")
    answer = input("    > ").lower()
    if answer == "bicycle":
        print('\n- "It might take a whole day to get to the grocery store and I hope to get home before it gets dark."')
    elif answer == "bus":
        print('\n- "I am glad that I decided to take a bus to get to the grocery store since it is really hot outside."')
    elif answer == "taxi":
        print('\n- "It might be quiet pricy but I think I can get all the ingredients before the sun goes down."')
    else:
        select_transportation()

def get_collected_items():
    return " ".join(collected_items)

def grocery_room():
    print("\n- How do you want to get to the market?")
    count = 1
    for transportation in transportations:
        print(f"    - Option {count}: There is {transportation} to get to the grocery store.")
        count += 1
    select_transportation()
    
    print('\n- Player arrived to the grocery store and went into the enterance')
    
    print('\n- "Hi, Which items are you looking for today? We just in stock few items but may not have everything that you are looking for" \n   - |Banana| |Sugar| |Cornstarch| |Baking-Soda| |Whipped-Cream| |Flour| |Chocolate| |Butter| |Milk| |Salt|\n')
    print("\n- Please type ONE ITEM at the time IDENTICALLY in the list. When you are done, type done.")
    while True:
        answer = input("    > ")
        if answer in items_in_store:
            collected_items.append(answer)
            items_in_store.remove(answer)
            if answer in required_ingredients:
                required_ingredients.remove(answer)
        elif "done" in answer:
            break
        else:
            print("That item is not in the store.")
    print("These are your remaining required ingredients:", required_ingredients)
    if len(required_ingredients) == 0:
        print("'Let's go back home to bake a strawberry fruit pie since we collected all the required ingredients'")
        print("\n- How do you want to get to the Mushroom village?")
        select_transportation()
        print(mushroom)
        print("\n-The player arrived to the Mushroom village. ")
        home()
    else:
        print('"We still have to collect strawberries in the forest. Let\'s try to go back to the Mushroom village."')
        print("\n- How do you want to get to the Mushroom village?")
        select_transportation()
        print(mushroom)
        print("\n-The player arrived to the Mushroom village. ")
        main_room()

def main_room(): 
    print("- Should I go to the forest to get the strawberries? or should I go to the grocery store to get other ingredients?")
    answer = input("    > ").lower()
    if answer == "grocery store":
        grocery_room()
    elif answer == "forest":
        forest_room()
    else:
        print("\n- Please type: Grocery Store or Forest\n")
        main_room()

def left_or_right_question(question):
    print(question)
    while True:
        response = input("    > ").lower()
        if response == "right" or response == "left":
            return response
        else:
            print("Please type either left or right.")

def forest_room():
    print(forest)
    response = left_or_right_question("\n- There are two ways to get through the forest. Should I go to the left? or should I go to the right?")
    if response == "left":
        print('\n- There isn\'t a way. I think we should go back to the forest.')
        forest_room()
    elif response == "right":
        response = left_or_right_question('\n- There is a footprint to the left path. Should I go to the left? or should I go to the right?')
        if response == "left":
            print("Oh no! I encounterd a fox! I cannot do this anymore. I am going home.")
            trap_room()
        elif response == "right":
            response = left_or_right_question('\n- I found a small pond and there are two ways to go through the forest. Should I go to the left? or should I go to the right?')
            if response == "left":
                response = left_or_right_question('\n- I can smell the strawberries around here. Which way should I go next? Should I go to the left? or should I go to the right?')
                if response == "right":
                    print('\n- I found the strawberries! Now let\'s go back to the main room and make sure that we have all the ingredients to bake a strawberry fruit pie."')
                    required_ingredients.remove("Strawberries")
                    print("These are your remaining required ingredients:", required_ingredients)
                    if len(required_ingredients) == 0:
                        print("'Let's go back home to bake a strawberry fruit pie since we collected all the required ingredients'")
                        home()
                    else:
                        print("'We still have to collect few required ingredients from the grocery store. Let's try to go back to the Mushroom village.'")
                        print(mushroom)
                        main_room()

                elif response == "left":
                    print("Oh no! There are tons of poisonous spiders in here! I need to get out from here before they bite me!")
                    trap_room()
            elif response == "right":
                trap_room()

    else:
        print("\n Please type: Left or Right")
        forest_room()

# Start
print("- This is a story-telling game which let users to choose the path of the game upon giving an option / intro\n")
print(f"- These are the ingredients required to make a strawberry fruit pie: {display_required_items}")
print("    - |Flour| & |Butter| & |Salt| are needed to make a crusted pie \n    - |Strawberries| & |Sugar| & |Cornstarch| & |Whipped-Cream| are needed to complete making a Strawberry fruit pie.\n")
main_room()

# required_ingredients = "| "
# ingredients = ["Strawberry","flour"]
# for ingredient in ingredients:
#     required_ingredients += (ingredient) + " | "
# print(required_ingredients)

# print(f"The required ingredients are {', '.join(ingredients)}")
# answer = input("> ")


    # Required_Ingredients

    # add 6 strawberries as requirements for ingredients 


# def forest_room():
#     print("\n- There are two ways to get through the forest. Should I go to the left? or should I go to the right?")
#     response = input("    >")
#     while True: 
#     if response == "Left":
#         print('\n- There isn\'t a way. I think we should go back.')
#         forest_room()
#     elif response == "Right":
#         print('\n- There is a footprint to the left path. Should I go to the left? or should I go to the right?')
#         response = input("    > ")
#         if response == "Left":
#             print("Oh no! I encounterd a fox! I cannot do this anymore. I am going home.")
#             trap_room()
#         elif response == "Right":
#             print('\n- I found a small pond and there are two ways to go through the forest. Should I go to the left? or should I go to the right?')
#             response = input("    >")
#             if response == "Left":
#                 print('\n- I can smell the strawberries around here. Which way should I go next? Should I go to the left? or should I go to the right?')
#                 response = input("    >")
#                 if response == "Right":
#                     print('\n- I found the strawberries! Now let\'s go back to the main room and make sure that we have all the ingredients to bake a strawberry fruit pie."')
#                     required_ingredients.remove("Strawberries")
#                     main_room()
#                 elif response == "Left":
#                     print("Oh no! There are tons of poisonous spiders in here! I need to get out from here before they bite me!")
#                     trap_room
#             elif response == "Right":
#                 trap_room
#     else:
#         print("\n Please type: Left or Right")
#         forest_room()