# IMPORTS ---------------------------------------
import os
import sys

import random
from termcolor import colored


# GLOBAL VARIABLES ------------------------------
keys_123 = "1 2 3"
keys_m = "M"
# IMPORTS ---------------------------------------
import os
import sys

import random
from termcolor import colored


# VARIABLES ------------------------------
keys_123 = ["1", "2", "3"]
keys_m = "M"
keys_launch_menu_quit = ["L", "Q"]
yes_no_keys = ["Y", "N"]
keys_grid = [5, 8, 12]

ships_sunk = 0
hits = 0

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12}

if len(sys.argv) > 1:
    player_name = sys.argv[1]

# GAME INTRO, MENU AND INSTRUCTION FUNCTIONS--------------------------
def launch_intro():
    """
    Initial function that loads Intro and requests players name
    """
    while True:
        print(colored('****************************************************************************************** \n', 'green'))
        print(colored("B A T T L E S H I P   B L A S T \n", 'green'))
        global player_name
        player_name = input(colored("Enter player name: \n", 'green')).title()

        if validate_player_name(player_name):
            break

def game_menu():
    """
    Presents user with menu uptions.
    Instruction page, launch game or exit game.
    """
    while True:
        print(colored('****************************************************************************************** \n', 'green'))
        print(colored("G A M E    M E N U \n", 'green'))
        print(colored("War is imminent....", 'green'))
        print(colored(f'{player_name}, prepare for battle! \n', 'green'))
        print(colored("Instructions--> 1", 'green'))
        print(colored("Launch game--> 2", 'green'))
        print(colored("Exit --> 3", 'green'))
        menu_selection = input('\n')
        if validate_key(menu_selection, keys_123):
            break
    if menu_selection == "1":
        game_instructions()
    elif menu_selection == "2":
        grid_choice()
        #launch_game()
    elif menu_selection == "3":
        exit_game()

def game_instructions():
    """
    Game instructions
    """
    while True:
        print(colored('******************************************************************************** \n', 'green'))
        print(colored("G A M E  I N S T R U C T I O N S \n", 'green'))
        print(colored("• Battlefield display: 5 x 5.", 'green'))
        print(colored("• There here are 5 hidden battleships.\n", 'green'))
        print(colored("• Rows : A, B, C, D, E", 'green'))
        print(colored("• Columns: 1, 2, 3, 4, 5", 'green'))
        print(colored("• Each ship takes up one coordinate", 'green'))
        print(colored("• For example: (A, 1)\n", 'green'))
        print(colored("• Enter coordinates to launch missil. \n", 'green'))
        print(colored("• You have a total of 15 missils.", 'green'))
        print(colored("• Sink ALL ships to win the game. \n", 'green'))
        print(colored("• Top left: (A, 1)", 'green'))
        print(colored("• Bottom right: (E, 4)\n", 'green'))
        print(colored("Go back to menu--> M", 'green'))
        menu_selection = input('\n').upper()
        if validate_key(menu_selection, keys_m):
            break
    if menu_selection == "M":
        game_menu()

# GAME ROUND FUNCTIONS--------------------------
def grid_choice():
    """ 
    Function to select grid size.
    """
    print(colored('******************************************************************************** \n', 'green'))
    print(colored("G R I D  S I Z E", 'green'))
    print("\n")
    print(colored("Please select grid size", 'green'))
    print(colored("5 x 5 --> 5", 'green'))
    print(colored("8 x 8 --> 8", 'green'))
    print(colored("12 x 12 --> 12", 'green'))
    while True:
        global grid_size
        grid_size = int(input('\n'))
        if validate_key(grid_size, keys_grid):
            break

    global keys_player_guess_row
    global keys_player_guess_column

    keys_player_guess_column = []
    for i in range(1,grid_size+1):
        keys_player_guess_column.append(i)

    keys_player_guess_row = []
    for i in range(65, 65 + grid_size):
        keys_player_guess_row.append(chr(i))
 
    global board
    board = []
    for x in range(grid_size):
        board.append([" . "] * grid_size)
    launch_game()

def grid(board):
    """
    Function that prints board onto the terminal
    """
    if grid_size == 5:
        print(colored("    1   2   3   4   5", 'green'))
        print(colored("  _____________________", 'green'))

    elif grid_size == 8:
        print(colored("    1   2   3   4   5   6   7   8", 'green'))
        print(colored("  __________________________________", 'green'))

    elif grid_size == 12:
        print(colored("    1   2   3   4   5   6   7   8   9  10  11  12", 'green'))
        print(colored("  _________________________________________________", 'green'))

    row_letter = 0
    for row in board:
        print(colored((chr(row_letter+65)+("| "))+(" ").join(row)+(" |"), 'green'))
        row_letter += 1
    if grid_size == 5:
        print(colored("  _____________________", 'green'))
    elif grid_size == 8:
        print(colored("  __________________________________", 'green'))
    elif grid_size == 12:
        print(colored("  _________________________________________________", 'green'))

def place_random_ships():
    """
    Function that generated 5 random unique coordinates.
    Battleships will be hidden on the board.
    """
    global enemy_ship_coordinates
    enemy_ship_coordinates = []
    while len(enemy_ship_coordinates) < int(grid_size):
        ship_row = random.randint(0, int(grid_size)-1)
        ship_column = random.randint(0, int(grid_size)-1)
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
    global ships_sunk
    global hits
    ships_sunk = 0
    hits = 0
    misiles = 0
    place_random_ships()
    print(enemy_ship_coordinates)
    while misiles <= 14:
        if ships_sunk == 5:
            break
        print(colored('******************************************************************************** \n', 'green'))
        print(colored("T H E    B A T T L E F I E L D \n", 'green'))
        print("\n")
        grid(board)
        print("\n")
        misiles_left = 15 - misiles
        print(colored(f'You have {misiles_left} misiles left!\n', 'green'))

        while True:
            row_choice_letter = input(colored("Enter row: \n", 'green')).upper()
            if validate_key(row_choice_letter, keys_player_guess_row):
                break
        while True:
            column_choice_number = int(input(colored("Enter column: \n", 'green')))
            if validate_key(column_choice_number, keys_player_guess_column):
                break
        row_choice = letters_to_numbers[row_choice_letter]
        column_choice = column_choice_number - 1
        global player_guess
        player_guess = row_choice, column_choice
        print(colored(f'You guessed ({row_choice_letter}, {column_choice_number}) \n', 'green'))
        compare_coordinates(board)
        misiles += 1
        print("\n")
        print(colored("Launch next misile--> L", 'green'))
        print(colored("Quit Game--> Q", 'green'))
        print(colored("If Q, all advances will be lost.", 'green'))

        while True:
            exit_option = input('\n').upper()
            if validate_key(exit_option, keys_launch_menu_quit):
                break
        if exit_option == "Q":
            break
        elif exit_option == "L":
            pass
    end_score()

def compare_coordinates(board):
    """
    Function that compares player guess and random coord.
    Determine wether ship is hit or missed.
    Prints a message on the screen.
    Prints an X (hit) or a - (miss) on the grid.
    """
    print(colored('******************************************************************************** \n', 'green'))
    print("\n")
    global hits
    global ships_sunk
    if (board[row_choice][column_choice]) == " X ":
        grid(board)
        print("\n")
        print(colored("You've already hit this target.", 'green'))
        print(colored("Try again!! \n", 'green'))
    elif (board[row_choice][column_choice]) == " - ":
        grid(board)
        print("\n")
        print(colored("You've already hit this target.", 'green'))
        print(colored("Try again!! \n", 'green'))
    elif player_guess in enemy_ship_coordinates:
        board[row_choice][column_choice] = " X "
        grid(board)
        print("\n")
        print(colored("You sunk a ship! \n", 'green'))
        hits += 1
        ships_sunk += 1
    elif player_guess not in enemy_ship_coordinates:
        board[row_choice][column_choice] = " - "
        grid(board)
        print("\n")
        print(colored("You missed! \n", 'green'))

def end_score():
    """
    End of rounds displaying final score.
    Requests play again or exit game.
    """
    print(colored('******************************************************************************** \n', 'green'))
    print("\n")
    if ships_sunk < 5:
        print(colored("G A M E  O V E R \n", 'green'))
        print("\n")
        print(colored(f"{player_name}, you lose... \n", 'green'))
        print(colored(f'{ships_sunk} ships sunk. \n', 'green'))
        print(colored(f'{5 - ships_sunk} ships remain. \n', 'green'))
        print("\n")
    elif ships_sunk == 5:
        print(colored("V I C T O R Y ! \n", 'green'))
        print(colored(f"{player_name}, you sank all enemy ships! \n", 'green'))
        print("\n")
    print(colored("Play again?", 'green'))
    print(colored("Yes--> Y", 'green'))
    print(colored("No--> N", 'green'))
    while True:
        exit_option = input(colored('\n', 'green')).upper()
        if validate_key(exit_option, yes_no_keys):
            break
    if exit_option == "N":
        game_over()
    elif exit_option == "Y":
        os.execv(sys.executable, ['python'] + sys.argv + [player_name])


def exit_game():
    """
    Exit Game
    """
    while True:
        print(colored('******************************************************************************** \n', 'green'))
        print(colored("Q U I T   G A M E \n", 'green'))
        print(colored("The enemy is so close... \n", 'green'))
        print(colored("Will you admit defeat and quit now? \n", 'green'))
        print(colored("Yes, quit now--> Y", 'green'))
        print(colored("No--> N", 'green'))
        exit_choice = input('\n').upper()
        if validate_key(exit_choice, yes_no_keys):
            break
    if exit_choice == "Y":
        game_over()
    elif exit_choice == "N":
        game_menu()

def game_over():
    """
    Function that triggers display of GAME OVER page
    """
    print(colored('******************************************************************************** \n', 'green'))
    print(colored("G A M E    O V E R", 'green'))
    print(colored("To play again, click on RUN PROGRAM", 'green'))

# VALIDATING FUNCTIONS--------------------------
def validate_key(data, valid_keys):
    """
    Function that validates data.
    """
    try:
        if data not in valid_keys:
            raise ValueError(
                f"Input--> {data}. Only {valid_keys} are valid inputs."
            )
    except ValueError as e:
        print(f"Invalid data: {e}")
        return False
    return True

def validate_player_name(data):
    """
    Function validating player name.
    """
    try:
        if (data.isalpha()) is False:
            raise ValueError(
                f'You entered {data} which is not an alphabetical string,'
            )
    except ValueError as e:
        print(f"Invalid data: {e}")
        return False
    return True

if len(sys.argv) == 1:
    launch_intro()

game_menu()



