transportations = ["Bicycle", "Bus", "Taxi"]
collected_items = []

def main_room(answer): 
    rooms_available = ["Market", "Forest"]
    if answer == "Grocery Store":
        print("How do you want to get to the market?")
        count = 1
        for transportation in transportations:
            print(f"Option {count}: There is {transportation} to get to the grocery store.")
            count += 1

        # transportation(method_of_transportation)
    # elif rooms_available == "Forest":

        # go to the forest

# every room make a list

def transportation(answer):
    if answer == "Bicycle":
        print("It might take a whole day to get to the grocery store and I hope to get home before it gets dark.")
    elif answer == "Bus":
        print("I am glad that I decided to take a bus to get to the grocery store since it is really hot outside.")
    elif answer == "Taxi":
        print("I w")



# starts
print("This is a story-telling game which lets users to choose the path of the game upon giving an option / intro")
Required_Ingredients = ["x"]
print("Should I go to the forest to get the strawberries first? or should I go to the grocery store to get the other ingredients first?")
answer = input("> ")
main_room(answer)

    # Required_Ingredients


