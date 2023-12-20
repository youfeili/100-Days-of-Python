print("Welcome to Treasure Island.\nYour mission is to find the treasure")

first = input("You're at a cross road. Where do you want to do? Type 'left' or 'right'\n")

if first == 'left':
    second = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if second == 'wait':
        third = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
        if third == 'red':
            print("Burned by fire.\nGame Over.")
        elif third == 'yellow':
            print("You Win!")
        elif third == 'blue':
            print("Eaten by beasts.\nGame Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")