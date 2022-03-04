import random

def generate_random_coordinates():
    """
    Function that generated 5 random unique 
    coordinates where battleships will
    be hidden on the board.
    """
    random_coordinates = []
    while len(random_coordinates) < 5:
        x = random.randint(0,4)
        y = random.randint (0,4)
        coordinate = x,y
        if coordinate not in random_coordinates:
            random_coordinates.append(tuple(coordinate))
    print(random_coordinates)
    
generate_random_coordinates()()
