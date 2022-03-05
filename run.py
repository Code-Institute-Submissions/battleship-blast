import random

from pyfiglet import Figlet
from termcolor import colored

def launch_intro():
    """
    Initial function that loads Intro 
    and requests players name
    """
    print(colored('************************************************ \n','green'))
    print(colored("B A T T L E S H I P   B L A S T \n",'green'))
    global player_name
    player_name = input(colored("Enter player name  \n",'green'))

def game_menu():
    """
    Presents user with menu uptions: 
    Instruction page, launch game or
    exit game.
    """
    print(colored('************************************************ \n','green'))
    print(colored("G A M E    M E N U \n",'green'))
    print("\n")
    print(colored("War is imminent....",'green'))
    print(colored(f'{player_name}, prepare for battle! \n','green'))
    print(colored("Game Instructions--> 1",'green'))
    print(colored("Launch game--> 2",'green'))
    print(colored("Exit game--> 3",'green'))
    global menu_selection
    menu_selection=input()
    menu_key_options(menu_selection)
    validate_key(menu_selection)

def validate_key(data):
    """
    Function that validates input data and raises errors accordingly.
    Correct data should be either 1, 2 or 3
    """
    try:
        keys="1 2 3"
        if data not in keys:
            raise ValueError(
                f"Only input 1, 2, 3 are valid. You provided invalid data {data}."
            )
    except ValueError as e:
        print(f"Invalid data: {e}")


def game_instructions():
    """
    Game instructions
    """
    print(colored('************************************************ \n','green'))
    print(colored("G A M E    I N S T R U C T I O N S \n",'green'))
    print("\n")
    print(colored("• The battlefield is displayed in a 5 x 5 grid.",'green'))
    print(colored("• In this field there are 5 battleships hidden.",'green'))
    print(colored("• Each battleship takes up one single coordinate. For example: (0, 1) \n",'green'))
    print(colored("• Enter the coordinates to launch the missil. \n",'green'))
    print(colored("• You have a total of 15 missils.",'green'))
    print(colored("• You must sink ALL battleships to defeat the enemy. \n",'green'))
    print(colored("• The top left corner is coordinate. (0, 0)",'green'))
    print(colored("• The bottom right corner is coordinates.\n (4, 4)",'green'))
    print("\n")
    print(colored("Go back to menu--> M",'green'))
    menu_selection= input().upper() 
    validate_key(menu_selection)
    menu_key_options(menu_selection)  

def launch_game():
    """
    Start Game
    """
    print('Start Game')

def exit_game():
    """
    Exit Game
    """
    print('Exit Game')

def menu_key_options(key_selection):
    """
    Function that directs the user to their chosen 
    option
    """
    if key_selection == "1":
        game_instructions()
    elif key_selection == "2":
        launch_game()
    elif key_selection == "3":
        exit_game()
    elif key_selection == "M":
        game_menu()

def generate_random_coordinates():
    """
    Function that generated 5 random unique 
    coordinates where battleships will
    be hidden on the board.
    """
    global random_coordinates
    random_coordinates = []
    while len(random_coordinates) < 5:
        x = random.randint(0,4)
        y = random.randint(0,4)
        coordinate = x,y
        if coordinate not in random_coordinates:
            random_coordinates.append(tuple(coordinate))
    return random_coordinates

launch_intro()
game_menu()

#generate_random_coordinates()
#print(random_coordinates)
