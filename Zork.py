import random
import time

# Function prints readable messages​​

def print_pause(sleep):
    print(sleep)
    time.sleep(2)

# function for validating the players input

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, please try again.")
    return response


# Player gets an introduction


def intro():
    print_pause("You find yourself in a mysterious room.")
    print_pause("How did you get here?")
    print_pause("You look around.")
    print_pause("The room seems empty.")
    print_pause("No wait...two doors appear in front of you.")
    print_pause("One is red and one is black.")

# function for random input of monsters


def random_monster():
    monster = random.choice(['troll', 'vampire', 'wolf'])
    if 'troll' == monster:
        print_pause("Oh no! A scary troll")
    elif 'troll' == monster:
        print_pause("Oh goodness! A creepy vampire!")
    elif 'wolf' == monster:
        print_pause("Look out, there's a wolf in front of you!")
    return monster


# function for red door


def red_door(tools):
    print_pause("You walk through the red door.")
    print_pause("You find yourself in a huge forest.")
    print_pause("This forest is strange...")
    print_pause("You seem to be lost in the woods.")
    if "coin" in tools:
        print_pause("Did you just hear something?")
        print_pause("It's moving closer from behind a tree.")
        random_monster()
        fight_option()
        print_pause("Oops. Your enemy just swallowed your coin. "
                    "You will need a sword to combat your enemy.")
        print_pause(" G A M E   O V E R ")
    else:
        print_pause("You really could use a tool right now.")
        print_pause("You search the area..")
        print_pause("You find a shiny object lying on the ground.")
        print_pause("It looks like a silver coin.")
        print_pause("You pick up the coin and return to the room.")
        tools.append("coin")
        door_call(tools)


# Function for black door


def black_door(tools):
    print_pause("You walk through the black door.")
    print_pause("You find yourself on a beautiful beach.")
    if "coin" in tools:
        print_pause("You find a great spot right there in the sun. ")
        print_pause("Auch! What did you just sit on?")
        print_pause("Seems to be a magic sword. \n"
                    "It might come in handy.")
        print_pause("You pick up the sword.")
        tools.append("sword")
        if "sword" in tools:
            print_pause("Everything is just great..."
                        "At least you thought..")
            print_pause("Oh no! Danger ahead! Is it a monster?")
            random_monster()
            fight_option()
            print_pause("Fortunately your sword is the right tool. \n"
                        "It got really scared and ran off. Phew! "
                        "What was it doing on a beach anyway..?")
            print_pause("CONGRATULATIONS! You won the game!")
    else:
        print_pause("It seems a bit too hot here. "
                    "You decide to walk back to the room.")
        door_call(tools)


# Checks if the player enters red or black door


def door_call(tools):
    choice = valid_input(
                        "Please enter the color of the door,"
                        "you would like to enter: \n",
                        "red", "black")
    if "red" == choice:
        red_door(tools)
    elif "black" == choice:
        black_door(tools)

# Checks if the player wants to fight the monster


def fight_option():
    response = valid_input(
                            "Are you ready to fight? \n"
                            "'1' if you're ready to fight! \n"
                            "'2' if you're too tired for that.\n",
                            "1", "2")
    if '1' in response:
        print_pause("Yes, let's go defeat your enemy!")
    if '2' in response:
        print_pause("Ok, thank you for playing.")
        play_again()


# Checks if the player wants to play again or end the game


def play_again():
    response = valid_input(
                        "Would you like to try again? "
                        "Please say 'yes' or 'no'.\n",
                        "yes", "no")
    if "yes" in response:
        print_pause("Ok, let's have another go!")
        play_game()
    if "no" in response:
        print_pause("OK, Thank you for playing.")

# Calling the functions


def play_game():
    intro()
    tools = []
    door_call(tools)
    play_again()

# The entry level

if __name__ == "__main__":
    play_game()