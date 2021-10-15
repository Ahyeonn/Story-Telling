from ascii_art import *

collected_items = []
transportations = ["Bicycle", "Bus", "Taxi"]
items_in_store = ["Banana","Sugar","Cornstarch","Baking-Soda","Whipped-Cream","Flour","Chocolate","Butter","Milk","Salt"]
required_ingredients = ["Strawberries","Sugar","Cornstarch","Whipped-Cream","Flour","Butter","Salt"]
display_required_items = "|Strawberries| |Sugar| |Cornstarch| |Whipped-Cream| |Flour| |Butter| |Salt|"

def trap_room():
    print("\n- You lost the game 💀 \n")
    return False

def home():
    print(display_home)
    print('\n- "I have collected:"', collected_items)
    print(f'\n- "All of the required ingredients are ready to be turned into a YUMMY strawberry fruit pie." {happy}')
    print('\n- "Thank you for helping me out with making the most delicious strawberry fruit pie in the world!" 🤩 ') 
    print(pie)
    print("\n- You won the game! 👏 👏 👏 \n")

def select_transportation():
    print("\n- Please type: Bicycle, Bus, or Taxi")
    answer = input("    > ").lower()
    if answer == "bicycle":
        print(bicycle)
        print('\n- "It might take a whole day to get to the place and I hope to get home before it gets dark." 🚲 ')
    elif answer == "bus":
        print(bus)
        print('\n- "I am glad that I decided to take the bus to get to the place since it is really hot outside." 🚌 ')
    elif answer == "taxi":
        print(taxi)
        print('\n- "It might be quite pricy, but I think I can get all of the ingredients before the sun goes down." 🚕 ')
    else:
        select_transportation()

def get_collected_items():
    return " ".join(collected_items)

def grocery_room():
    print("\n- How do you want to get to the grocery store? 🛒 ")
    for transportation in transportations:
        print(f"    - There is a {transportation} to get to the grocery store.")
    select_transportation()
    
    print('\n- Player arrived at the grocery store 🛒 and went into the entrance.')
    
    print('\n- "Hi 👋 , Which items are you looking to purchase today? We are in stock for a few items, but may not have everything that you are looking for." - Grocery Worker')
    print('    ----------------------------------------------------------------------------------------------------------')
    print('      |Banana| |Sugar| |Cornstarch| |Baking-Soda| |Whipped-Cream| |Flour| |Chocolate| |Butter| |Milk| |Salt| ')
    print('    ----------------------------------------------------------------------------------------------------------\n')
    print("- Please type ONE ITEM at a time IDENTICALLY to the list. When you are DONE, type done.")
    while True:
        answer = input("    > ")
        if answer in items_in_store:
            collected_items.append(answer)
            items_in_store.remove(answer)
            print(f'\n- These items are currently available in the market:\n    -{items_in_store}\n')
            if answer in required_ingredients:
                required_ingredients.remove(answer)
        elif answer in collected_items:
            print("\n- You already have this item in the cart ❗")
        elif "done" in answer:
            print('\n- "Thank you for coming to our grocery store. 🛒 See you next time again!" 👋  - Grocery Worker')
            break
        else:
            print('\n- "That item is not available in the store. ❌ "')
    print("\n- These are your remaining required ingredients:", required_ingredients)
    if len(required_ingredients) == 0:
        print('\n- "Let\'s go back home to make a strawberry fruit pie 🥧 since we collected all of the required ingredients."')
        print("\n- How do you want to get to the Mushroom village? 🍄 ")
        select_transportation()
        print(mushroom)
        print("\n- The player arrived at the Mushroom village. 🍄 ")
        print("\n- Player has arrived home. 🏡 ")
        home()
    else:
        print('\n- "We still have to collect a few ingredients to make a strawberry fruit pie. Let\'s try to go back to the Mushroom village. 🍄 "')
        print("\n- How do you want to get to the Mushroom village? 🍄 ")
        select_transportation()
        print(mushroom)
        print("\n- The player has arrived at the Mushroom village. 🍄 \n")
        main_room()

def main_room(): 
    print("- Should I go to the forest 🌲 to get the strawberries or should I go to the grocery store 🛒 to get the other ingredients?")
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
            print("\n- Please type: Left or Right")

def forest_room():
    print(forest)
    response = left_or_right_question("\n- There are two ways to get through the forest. Should I go to the left or should I go to the right?")
    if response == "left":
        print('\n- "There isn\'t a way. ⛔  I think we should go back to the forest."')
        forest_room()
    elif response == "right":
        response = left_or_right_question('\n- There is a footprint 👣 on the left path. Should I go to the left or should I go to the right?')
        if response == "left":
            print('\n- "Oh no! I encounterd a fox! 🦊 I cannot do this anymore. I am going home."')
            trap_room()
        elif response == "right":
            response = left_or_right_question('\n- I found a small pond 🏞️  and there are two ways to go through the forest. Should I go to the left or should I go to the right?')
            if response == "left":
                response = left_or_right_question('\n- I can smell the strawberries 🍓 around here. Which way should I go next? Should I go to the left or should I go to the right?')
                if response == "right":
                    if "Strawberries" in required_ingredients:
                        print('\n- "I found the strawberries! 🍓 Now let\'s go back to the mushroom village 🍄 and make sure that we have all the ingredients to bake a strawberry fruit pie."')
                        required_ingredients.remove("Strawberries")
                        print("\n    - These are your remaining required ingredients:", required_ingredients)
                    else:
                        print("\n- These are your remaining required ingredients:", required_ingredients)
                        print('\n- "We don\'t need anymore strawberries since we have already collected some❗ "')
                    if len(required_ingredients) == 0:
                        print('\n- "Since we collected all the required ingredients, let\'s go back home 🏠 to bake a strawberry fruit pie "')
                        home()
                    else:
                        print('\n- "We still have to collect a few required ingredients from the grocery store. 🛒  Let\'s try to go back to the Mushroom village. 🍄 "')
                        print(mushroom)
                        main_room()

                elif response == "left":
                    print('\n- "Oh no! There are tons of poisonous spiders 🕷️  in here! I need to get out of here before they bite me! 💨 "')
                    trap_room()
            elif response == "right":
                print('\n- "Ouchh! I stumbled on a rock! 🪨  I should go back home and disinfect my wound. 🩹 "')
                trap_room()

    else:
        print("\n Please type: Left or Right")
        forest_room()

# Start
print(hi)
print("- This is a story-telling game which allows users to select from a few options to choose a specific path to collect ingredients in order to make a strawberry fruit pie. 🥧 \n")
print(f"- These are the ingredients required to make a strawberry fruit pie: {display_required_items}")
print("    - |Flour 🫓  | & |Butter 🧈 | & |Salt 🧂| are needed to make a pie crust. \n    - |Strawberries 🍓| & |Sugar 🧂| & |Cornstarch 🌽 | & |Whipped-Cream 🥛| are needed to make the topping for the Strawberry fruit pie.\n")
main_room()
