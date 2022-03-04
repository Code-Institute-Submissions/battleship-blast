from termcolor import colored

import random

def launch_intro():
    """
    Initial function that loads Intro 
    and requests players name
    """
    print(colored("WELCOME TO BATTLESHIPS BLAST \n",'green'))


def generate_random_coordinates():
    """
    Function that generated 5 random unique 
    coordinates where battleships will
    be hidden on the board.
    """
    random_coordinates = []
    while len(random_coordinates) < 5:
        x = random.randint(0,4)
        y = random.randint(0,4)
        coordinate = x,y
        if coordinate not in random_coordinates:
            random_coordinates.append(tuple(coordinate))
    return random_coordinates
    

launch_intro()
generate_random_coordinates()
