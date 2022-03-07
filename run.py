# IMPORTS ---------------------------------------

import random

from pyfiglet import Figlet
from termcolor import colored

# GLOBAL VARIABLES ------------------------------
keys_123 = "1 2 3"
keys_m = "M"
keys_exit = "Y M"

# GAME INTRO, MENU AND INSTRUCTION FUNCTIONS--------------------------

def launch_intro():
    """
    Initial function that loads Intro 
    and requests players name
    """
    while True:
        print(colored('************************************************ \n','green'))
        print(colored("B A T T L E S H I P   B L A S T \n",'green'))
        global player_name
        player_name = input(colored("Enter player name: \n",'green'))

        if validate_player_name(player_name):
            break


def game_menu():
    """
    Presents user with menu uptions: 
    Instruction page, launch game or
    exit game.
    """
    while True:
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

        if validate_key(menu_selection, keys_123):
            break

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
    elif key_selection == "Y":
        game_over() 

def game_instructions():
    """
    Game instructions
    """
    while True:
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
        menu_key_options(menu_selection)  
        
        if validate_key(menu_selection, keys_m):
            break
  
def exit_game():
    """
    Exit Game
    """
    while True:
        print(colored('************************************************ \n','green'))
        print(colored("Q U I T   G A M E \n",'green'))
        print("\n")
        print(colored("The enemy is so close... \n",'green'))
        print(colored("Will you admit defeat and quit now? \n",'green'))
        print(colored("Quit game--> Y",'green'))
        print(colored("Go back to menu--> M",'green'))

        menu_selection= input().upper() 
        menu_key_options(menu_selection)  
        
        if validate_key(menu_selection, keys_exit):
            break
   
def game_over():
    """
    Function that triggers display of GAME OVER page
    """
    print(colored('************************************************ \n','green'))

    print(colored("G A M E    O V E R",'green'))



# VALIDATING FUNCTIONS--------------------------

def validate_key(data, valid_keys):
    """
    Function that validates input data and raises errors accordingly.
    Correct data should be either 1, 2 or 3
    """
    try:
        if len(data)!= 1:
            raise ValueError(
                f'String length--> {len(data)}. Type one value only.'
            )
        elif data not in valid_keys:
            raise ValueError(
                f"Input--> {data} Only {valid_keys} are valid inputs."
            )
       
    except ValueError as e:
        print(f"Invalid data: {e}")
        return False
    return True

def validate_player_name(data):
    """
    Function validating player name
    """
    try:
        if (data.isalpha()) == False:
            raise ValueError(
                f'You entered {data} which is not an alphabetical string,'
            )
    except ValueError as e:
        print(f"Invalid data: {e}")
        return False
    return True


# GAME ROUND FUNCTIONS--------------------------

board=[]
for x in range(5):
    board.append([" . "]*5)


def grid(board):
    """ 
    Function that prints board onto the terminal
    """
    print("    A   B   C   D   E")
    print("  _____________________")
    row_letter=0
    for row in board:
        print((chr(row_letter+65)+("| "))+(" ").join(row)+(" |"))
        row_letter+=1
    print("  _____________________")
    
def place_random_ships():
    """
    Function that generated 5 random unique 
    coordinates where battleships will
    be hidden on the board.
    """
    global enemy_ship_coordinates
    enemy_ship_coordinates = []
    while len(enemy_ship_coordinates) < 5:
        ship_row = random.randint(0,4)
        ship_column = random.randint(0,4)
        coordinate = ship_row, ship_column
        if coordinate not in enemy_ship_coordinates:
            enemy_ship_coordinates.append(tuple(coordinate))
    print(enemy_ship_coordinates)

def launch_game():
    """
    Start Game
    """
    print(colored('************************************************ \n','green'))
    print(colored("T H E    B A T T L E F I E L D \n",'green'))
    print("\n")
    grid(board)
    print("\n")
    global row_choice
    global column_choice
    missils=0
    place_random_ships()
    while missils<=15:
        row_choice = int(input(colored("Enter row coordinate: \n",'green')))
        column_choice = int(input(colored("Enter column coordinate: \n",'green')))
        global player_guess
        player_guess= row_choice, column_choice
        print(player_guess)
        missils+=1
        print(missils)
        compare_coordinates(board)

def compare_coordinates(board):
    """
    Function that compares player guess and randomly generated 
    coordinates to determine wether ship is hit or missed, 
    prints a message on the screen, and prints an X (hit) or a - (miss)
    on the grid.
    """
    print(colored('************************************************ \n','green'))
    print("\n")
    hits=0

    if player_guess in enemy_ship_coordinates:
        board[row_choice][column_choice]=" X "
        grid(board)
        print("\n")
        print(colored("You sunk a ship! \n",'green'))
        hits+=1
        print(hits)

    elif player_guess not in enemy_ship_coordinates:
        board[row_choice][column_choice]=" - "
        grid(board)
        print("\n")
        print("You missed!")
        


launch_intro()
game_menu()

