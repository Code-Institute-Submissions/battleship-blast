# IMPORTS ---------------------------------------
import random
from termcolor import colored

# GLOBAL VARIABLES ------------------------------
keys_123 = "1 2 3"
keys_m = "M"
keys_exit = "Y M"
keys_player_guess_row = "A B C D E "
keys_player_guess_column = "1 2 3 4 5"

letters_to_numbers = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4}

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
        menu_selection=input('\n')
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
        print(colored("• In this field there are 5 battleships hidden.\n",'green'))
        print(colored("• Rows : A, B, C, D, E,.",'green'))
        print(colored("• Columns: 1, 2, 3, 4, 5.",'green'))
        print(colored("• Each battleship takes up one single coordinate. For example: (A, 1) \n",'green'))
        print(colored("• Enter the coordinates to launch the missil. \n",'green'))
        print(colored("• You have a total of 15 missils.",'green'))
        print(colored("• You must sink ALL battleships to defeat the enemy. \n",'green'))
        print(colored("• The top left corner is coordinate. (A, 1)",'green'))
        print(colored("• The bottom right corner is coordinates.\n (E, 4)",'green'))
        print("\n")
        print(colored("Go back to menu--> M",'green'))
        menu_selection= input('\n').upper() 
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
        menu_selection= input('\n').upper() 
        menu_key_options(menu_selection)  
        if validate_key(menu_selection, keys_exit):
            break  

def game_over():
    """
    Function that triggers display of GAME OVER page
    """
    print(colored('************************************************ \n','green'))

    print(colored("G A M E    O V E R",'green'))

# GAME ROUND FUNCTIONS--------------------------
board=[]
for x in range(5):
    board.append([" . "]*5)

def grid(board):
    """ 
    Function that prints board onto the terminal
    """
    print("    1   2   3   4   5")
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

def launch_game():
    """
    Start Game round. 
    """
    global row_choice
    global column_choice
    global row_choice_letter
    global column_choice_number
    misiles=1
    place_random_ships()
    while misiles<=3:
        print(colored('************************************************ \n','green'))
        print(colored("T H E    B A T T L E F I E L D \n",'green'))
        print("\n")
        grid(board)
        print("\n")
        while True:
            row_choice_letter = input(colored("Enter row coordinate: \n",'green')).upper()
            validate_key(row_choice_letter, keys_player_guess_row)
            if validate_key(row_choice_letter, keys_player_guess_row):
                break
        while True:        
            column_choice_number = input(colored("Enter column coordinate: \n",'green')).upper()
            validate_key(column_choice_number, keys_player_guess_column)
            if validate_key(column_choice_number, keys_player_guess_column):
                break          
        row_choice = letters_to_numbers[row_choice_letter]
        column_choice = int(column_choice_number) - 1        
        global player_guess
        player_guess= row_choice, column_choice
        print(colored(f'You guessed ({row_choice_letter}, {column_choice_number}) \n','green'))
        compare_coordinates(board)
        misiles+=1
        print("\n")
        print(colored("Launch next misile--> L",'green'))
        print(colored("Menu--> M",'green'))
        print(colored("Quit Game--> Q",'green'))

        exit_option= input('\n').upper() 
        
       
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
    
    if (board[row_choice][column_choice]) ==" X ":
        grid(board)
        print(colored("You've already hit this target. Try again!! \n",'green')) 
        
    elif (board[row_choice][column_choice]) ==" - ":
        grid(board)
        print(colored("You've already hit this target. Try again!! \n",'green')) 
        
    elif player_guess in enemy_ship_coordinates:
        board[row_choice][column_choice]=" X "
        grid(board)
        print("\n")
        print(colored("You sunk a ship! \n",'green'))
        hits+=1
    elif player_guess not in enemy_ship_coordinates:
        board[row_choice][column_choice]=" - "
        grid(board)
        print("\n")
        print(colored("You missed! \n",'green'))  


   
# VALIDATING FUNCTIONS--------------------------

def validate_key(data, valid_keys):
    """
    Function that validates input data and raises errors accordingly.
    Reusable function: used to validate menu selection, used to validate 
    player row/column guess.
    """
    try:
        if len(str(data))!= 1:
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

launch_intro()
game_menu()

