# IMPORTS ---------------------------------------
import random
from termcolor import colored

# GLOBAL VARIABLES ------------------------------
keys_123 = "1 2 3"
keys_m = "M"
keys_exit = "Y M"
keys_player_guess_row = "A B C D E "
keys_player_guess_column = "1 2 3 4 5"
keys_launch_menu_quit = "L Q"
game_over_keys = "M Q"

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

# GAME INTRO, MENU AND INSTRUCTION FUNCTIONS--------------------------
def launch_intro():
    """
    Initial function that loads Intro and requests players name
    """
    while True:
        print(colored('********************************* \n', 'green'))
        print(colored("B A T T L E S H I P   B L A S T \n", 'green'))
        global player_name
        player_name = input(colored("Enter player name: \n", 'green'))

        if validate_player_name(player_name):
            break

def game_menu():
    """
    Presents user with menu uptions.
    Instruction page, launch game or exit game.
    """
    while True:
        print(colored('********************************** \n', 'green'))
        print(colored("G A M E    M E N U \n", 'green'))
        print("\n")
        print(colored("War is imminent....", 'green'))
        print(colored(f'{player_name}, prepare for battle! \n', 'green'))
        print(colored("Game Instructions--> 1", 'green'))
        print(colored("Launch game--> 2", 'green'))
        print(colored("Exit game--> 3", 'green'))
        global menu_selection
        menu_selection = input('\n')
        menu_key_options(menu_selection)
        if validate_key(menu_selection, keys_123):
            break

def menu_key_options(key_selection):
    """
    Function that directs the user to their chosen option
    """
    if key_selection == "1":
        game_instructions()
    elif key_selection == "2":
        launch_game()
    elif key_selection == "3":
        exit_game()
    elif key_selection == "M":
        game_menu()
    elif key_selection == "Y" or "Q":
        game_over()
    elif key_selection == "L":
        pass

def game_instructions():
    """
    Game instructions
    """
    while True:
        print(colored('************************ \n', 'green'))
        print(colored("G A M E  I N S T R U C T I O N S \n", 'green'))
        print("\n")
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
        print("\n")
        print(colored("Go back to menu--> M", 'green'))
        menu_selection = input('\n').upper()
        menu_key_options(menu_selection)
        if validate_key(menu_selection, keys_m):
            break

def exit_game():
    """
    Exit Game
    """
    while True:
        print(colored('******************* \n', 'green'))
        print(colored("Q U I T   G A M E \n", 'green'))
        print("\n")
        print(colored("The enemy is so close... \n", 'green'))
        print(colored("Will you admit defeat and quit now? \n", 'green'))
        print(colored("Quit game--> Y", 'green'))
        print(colored("Go back to menu--> M", 'green'))
        menu_selection = input('\n').upper()
        if validate_key(menu_selection, keys_exit):
            break

def game_over():
    """
    Function that triggers display of GAME OVER page
    """
    print(colored('***************************** \n', 'green'))

    print(colored("G A M E    O V E R", 'green'))

# GAME ROUND FUNCTIONS--------------------------
board = []
for x in range(5):
    board.append([" . "]*5)

def grid(board):
    """
    Function that prints board onto the terminal
    """
    print("    1   2   3   4   5")
    print("  _____________________")
    row_letter = 0
    for row in board:
        print((chr(row_letter+65)+("| "))+(" ").join(row)+(" |"))
        row_letter += 1
    print("  _____________________")

def place_random_ships():
    """
    Function that generated 5 random unique coordinates.
    Battleships will be hidden on the board.
    """
    global enemy_ship_coordinates
    enemy_ship_coordinates = []
    while len(enemy_ship_coordinates) < 5:
        ship_row = random.randint(0, 4)
        ship_column = random.randint(0, 4)
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
    misiles = 1
    place_random_ships()
    while misiles <= 3:
        print(colored('********************************\n', 'green'))
        print(colored("T H E    B A T T L E F I E L D \n", 'green'))
        print("\n")
        grid(board)
        print("\n")
        while True:
            row_choice_letter = input(colored("Enter row: \n", 'green')).upper()
            if validate_key(row_choice_letter, keys_player_guess_row):
                break
        while True:
            column_choice_number = input(colored("Enter column: \n", 'green')).upper()
            if validate_key(column_choice_number, keys_player_guess_column):
                break
        row_choice = letters_to_numbers[row_choice_letter]
        column_choice = int(column_choice_number) - 1
        global player_guess
        player_guess = row_choice, column_choice
        print(colored(f'You guessed ({row_choice_letter}, {column_choice_number}) \n', 'green'))
        compare_coordinates(board)
        misiles += 1
        print("\n")

        print(colored("Launch next misile--> L", 'green'))
        print(colored("Quit Game--> Q", 'green'))

        while True:
            exit_option = input('\n').upper()
            if validate_key(exit_option, keys_launch_menu_quit):
                break
        menu_key_options(exit_option)

        if exit_option == "Q":
            break
    end_score()

def compare_coordinates(board):
    """
    Function that compares player guess and random coord.
    Determine wether ship is hit or missed.
    Prints a message on the screen.
    Prints an X (hit) or a - (miss) on the grid.
    """
    print(colored('**************************** \n', 'green'))
    print("\n")
    hits = 0
    global ships_sunk
    ships_sunk = 0
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
    print(colored('**************************** \n', 'green'))
    print("\n")
    if ships_sunk < 5:
        print(colored("G A M E  O V E R \n", 'green'))
        print("\n")
        print(colored(f"{player_name}'s score: \n", 'green'))
        print(colored(f'{ships_sunk} ships sunk. \n', 'green'))
        print(colored(f'{5 - ships_sunk}ships remain. \n', 'green'))
        print("\n")
    elif ships_sunk == 5:
        print(colored("V I C T O R Y ! \n", 'green'))
        print(colored(f"{player_name}, you sank all enemy ships! \n", 'green'))
        print("\n")
    print(colored("Go back to menu--> M", 'green'))
    print(colored("Quit Game--> Q", 'green'))
    while True:
            exit_option = input(colored('Play again?\n', 'green')).upper()
            if validate_key(menu_key_options(exit_option), game_over_keys):
                break
    print(colored("Go back to menu--> M", 'green'))
    print(colored("Quit Game--> Q", 'green'))
    menu_key_options(exit_option)

# VALIDATING FUNCTIONS--------------------------
def validate_key(data, valid_keys):
    """
    Function that validates data.
    """
    try:
        if len(str(data)) != 1:
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
    Function validating player name.
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
