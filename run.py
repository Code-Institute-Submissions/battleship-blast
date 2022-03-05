from termcolor import colored
from pyfiglet import Figlet

import random

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
    print(colored("War is imminent....",'green'))
    print(colored(f'{player_name}, prepare for battle! \n','green'))
    print(colored("Game Instructions--> 1",'green'))
    print(colored("Launch game--> 2",'green'))
    print(colored("Exit game--> 3",'green'))
    global menu_selection
    menu_selection=int(input())


def game_instructions():
    """
    Game instructions
    """
    print('Game instructions')

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
    if key_selection == 1:
        game_instructions()
    elif key_selection == 2:
        launch_game()
    elif key_selection == 3:
        exit_game()
    else: 
        print('Invalid entry')
    
   


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
menu_key_options(menu_selection)
generate_random_coordinates()
print(random_coordinates)
