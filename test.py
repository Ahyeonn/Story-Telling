from ascii_art import *

collected_items = []
transportations = ["Bicycle", "Bus", "Taxi"]
items_in_store = ["Banana","Sugar","Cornstarch","Baking-Soda","Whipped-Cream","Flour","Chocolate","Butter","Milk","Salt"]
required_ingredients = ["Strawberries","Sugar","Cornstarch","Whipped-Cream","Flour","Butter","Salt"]
display_required_items = "|Strawberries| |Sugar| |Cornstarch| |Whipped-Cream| |Flour| |Butter| |Salt|"

def step_one_flour():
    print('\n- Please type: Continue or Give up')
    answer = input("    > ").lower()
    if answer == "continue":
        return True
    elif answer == "give up":
        print('\n- "The time that I spent & effort that I put in was useless."')
        trap_room()
    else:
        step_one_flour()

def trap_room():
    print("\n- You lost the game\n")
    return False

def home():
    print(display_home)
    print('\n- "I have collected:"', collected_items)
    print(f'\n- "All the required ingredients are ready to be baked into a YUMMY strawberry fruit pie!" {happy}')
    print('\n- "Let\'s find the recipe book to figure it out on how to bake a strawberry fruit pie."\n\n- "I have a strawberry fruit pie recipe book some where here...."')
    print(book)
    print('\n- Found the recipe book.')
    print('\n- "Oh no... My only strawberry fruit recipe book is teared in pieces." \n\n- "Should I continue to bake the strawberry fruit pie in scratch? or should I give up?"')
    

    print('\n- "I only remember some steps on how to bake a strawberry fruit pie but... LET\'S DO THIS!"')
    print('\n- "The first step is to make a pie crust for the strawberry fruit pie. I have |Flour| |Butter| |Salt| ready to make a pie crust."')
    print('\n- "I remember the first step is to mix flour, salt, and sugar before I put it into the food processor."')
    print('\n- "Hmmm... Should I add three cups of flour or should I add four cups of flour?"')
    step_one_flour()

    # print('\n- "Thank you for helping me out to bake a most delicious strawberry fruit pie in the world!"')
    # print(pie)
    # print("\n- You won the game!\n")

def select_transportation():
    print("\n- Please type: Bicycle, Bus, or Taxi")
    answer = input("    > ").lower()
    if answer == "bicycle":
        print(bicycle)
        print('\n- "It might take a whole day to get to the grocery store and I hope to get home before it gets dark."')
    elif answer == "bus":
        print(bus)
        print('\n- "I am glad that I decided to take a bus to get to the grocery store since it is really hot outside."')
    elif answer == "taxi":
        print(taxi)
        print('\n- "It might be quiet pricy but I think I can get all the ingredients before the sun goes down."')
    else:
        select_transportation()

def get_collected_items():
    return " ".join(collected_items)

def grocery_room():
    print("\n- How do you want to get to the market?")
    count = 1
    for transportation in transportations:
        print(f"    - Option {count}: There is a {transportation} to get to the grocery store.")
        count += 1
    select_transportation()
    
    print('\n- Player arrived to the grocery store and went into the enterance.')
    
    print('\n- "Welcome to Mushroom Dushroom, Which items are you looking for purchasing today? We just in stock few items but may not have everything that you are looking for." - Grocery Worker')
    print('    ----------------------------------------------------------------------------------------------------------')
    print('      |Banana| |Sugar| |Cornstarch| |Baking-Soda| |Whipped-Cream| |Flour| |Chocolate| |Butter| |Milk| |Salt| ')
    print('    ----------------------------------------------------------------------------------------------------------\n')
    print("- Please type ONE ITEM at the time IDENTICALLY in the list. When you are DONE, type done.")
    while True:
        answer = input("    > ")
        if answer in items_in_store:
            collected_items.append(answer)
            items_in_store.remove(answer)
            print(f'\n- These items are currently available in the market:\n    -{items_in_store}\n')
            if answer in required_ingredients:
                required_ingredients.remove(answer)
        elif answer in collected_items:
            print("\n- You already have this item in the cart.")
        elif "done" in answer:
            print('"Thank you for using our Mushroom Dushroom. See you next time again!" - Grocery Worker')
            break
        else:
            print('\n- "This item is currently not available in the store." - Grocery Worker')
    print("\n- These are your remaining required ingredients:", required_ingredients)
    if len(required_ingredients) == 0:
        print('\n- "Let\'s go back home to bake a strawberry fruit pie since we collected all the required ingredients"')
        print("\n- How do you want to get to the Mushroom village?")
        select_transportation()
        print(mushroom)
        print("\n- The player arrived to the Mushroom village.")
        home()
    else:
        print('\n- "We still have to collect strawberries in the forest. Let\'s try to go back to the Mushroom village."')
        print("\n- How do you want to get to the Mushroom village?")
        select_transportation()
        print(mushroom)
        print("\n- The player arrived to the Mushroom village.\n")
        main_room()

def main_room(): 
    print('- "Should I go to the forest to get the strawberries? or should I go to the grocery store to get other ingredients?"')
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
            print("\n- Please type: Left or Right.")

def forest_room():
    print(forest)
    response = left_or_right_question('\n- "There are two ways to get through the forest. Should I go to the left? or should I go to the right?"')
    if response == "left":
        print('\n- "There isn\'t a way. I think we should go back to the forest."')
        forest_room()
    elif response == "right":
        response = left_or_right_question('\n- "There is a footprint to the left path. Should I go to the left? or should I go to the right?"')
        if response == "left":
            print('\n- "Oh no! I encounterd a fox! I cannot do this anymore. I am going home."')
            trap_room()
        elif response == "right":
            response = left_or_right_question('\n- "I found a small pond and there are two ways to go through the forest. Should I go to the left? or should I go to the right?"')
            if response == "left":
                response = left_or_right_question('\n- "I can smell the strawberries around here. Which way should I go next? Should I go to the left? or should I go to the right?"')
                if response == "right":
                    print('\n- "I found the strawberries! Now let\'s go back to the mushroom village and make sure that we have all the ingredients to bake a strawberry fruit pie."')
                    required_ingredients.remove("Strawberries")
                    print("\n- These are your remaining required ingredients:", required_ingredients)
                    if len(required_ingredients) == 0:
                        print('\n- "Let\'s go back home to bake a strawberry fruit pie since we collected all the required ingredients"')
                        home()
                    else:
                        print('\n- "We still have to collect few required ingredients from the grocery store. Let\'s try to go back to the Mushroom village."')
                        print(mushroom)
                        main_room()

                elif response == "left":
                    print('\n- "Oh no! There are tons of poisonous spiders in here! I need to get out from here before they bite me!"')
                    trap_room()
            elif response == "right":
                print('\n- "Ouchh! I stumbled on the rock! I should go back home and disinfect my wound."')
                trap_room()

    else:
        print("\n Please type: Left or Right")
        forest_room()

# Start
print('- "I found the strawberries! 🍓 Now let\'s go back to the mushroom village and make sure that we have all the ingredients to bake a strawberry fruit pie."')
print(hi)
print("- This is a story-telling game which let users to select few options to choose the path to collect ingredients & to bake a strawberry fruit pie.\n")
print(f"- These are the ingredients required to make a strawberry fruit pie: {display_required_items}")
print("    - |Flour| & |Butter| & |Salt| are needed to make a crusted pie. \n    - |Strawberries| & |Sugar| & |Cornstarch| & |Whipped-Cream| are needed to complete making a Strawberry fruit pie.\n")
main_room()