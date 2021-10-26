"""
Basic idea:
- Player has x shots to sink ships randomly generated onto a grid.
- Ships will have varying sizes (of 2 to 5)
- Allow player to alter difficulty (either difficulty setting, or directly by changing grid size, # of ships or # of bullets)
- Attempt to keep gameplay resonably watchable in the terminal app.


What global variables do I need?
- grid (something that represents our grid)
- grid_size (how large a grid is used)
- number_of_ships (how many ships to place)
- shots_left (how many shots left before game is lost)
- ships_sunk (something to track fully sunk ships, to provide player info on their progress and to track if game is won)


What functions do I need?
def start_game  (once user confirms/inputs difficulty settings, this runs and builds the grid with ships)

def hit_miss  (check if user has hit a ship, and change icon accordingly)
    def hit
    def miss




Legend for Grid:
"." = Water (empty space)
"@" = Ship (only used backend)
"X" = Hit (damaged ship)
"0" = Miss (water that has been shot at, without hitting a ship)
"""

# Imports used to generate random ship placement, time to help ensure randomness
import random
import time

"""
The program utilized a fair amount of global variables, they are listed here.
"""
# A variable for the grid upon which the ships are places
grid = [[]]

# Variable with letters, used to create the grid later.
letters = "ABCDEFGHIJKL"

# Variable for the size of the grid.
grid_size = 10

# Variable for how many turns remain before the game is lost.
shots_left = 50

# Variable for number of ships
ship_count = 8

# Variable that tracks amount of ships sunk.
ships_sunk = 0

# Variable to remember chosen difficulty setting
game_lenght = 1

# Variable that stores information about where the ships randomly spawned
ship_location_storage = [[]]


def difficulty_setting(game_lenght):
    """
    A function to set grid_size, ship_count & shots_left 
    The variables differ dependant on users chosen game lenght.
    """
    # Global variables being modified inside this function
    global grid_size
    global ship_count
    global shots_left

    if game_lenght == 1:
        grid_size = 8
        ship_count = 5
        shots_left = 32
    elif game_lenght == 2:
        grid_size = 10
        ship_count = 8
        shots_left = 50
    else:
        grid_size = 12
        ship_count = 12
        shots_left = 72


def print_ship(y_coordinate_start, y_coordinate_end, x_coordinate_start, x_coordinate_end):
    """
    Function to print the ship onto the gameboard.
    Performs a check to ensure not ships end up on top of eachother.
    Then stores position into the ships_location_storage variable.
    ships_location_storage is used to check for hits and if game is won.
    """
    # Global variables being modified inside this function
    global ship_location_storage
    global grid

    empty_position = True
    # Check if we are trying to position a ship on a non water space
    for column in range(y_coordinate_start, y_coordinate_end):
        for row in range(x_coordinate_start, x_coordinate_end):
            if grid[column][row] != ".":
                empty_position = False
                break
    # If the coast is clear, we are ready to store the ships location
    if empty_position:
        ship_location_storage.append([y_coordinate_start, y_coordinate_end, x_coordinate_start, x_coordinate_end])
        for column in range(y_coordinate_start, y_coordinate_end):
            for row in range(x_coordinate_start, x_coordinate_end):
                grid[column][row] = "@"
    return empty_position


def check_position(column, row, size, heading):
    """
    Function that uses the randomly generated ship info from start_game.
    Combines the selected coordinate with lenght & heading to check if ship remains inside the grid.
    Calls support function that checks if the ship would collide with a previously placed ship.
    """
    # Global variables being modified inside this function
    global grid_size

    y_coordinate_start = column
    y_coordinate_end = column + 1
    x_coordinate_start = row
    x_coordinate_end = row + 1

    # Depending on which way the ship is heading we perform a different check.
    if heading == "up":
        if row - size < 0:
            return False
        x_coordinate_start = row - size + 1
    elif heading == "down":
        if row + size >= grid_size:
            return False
        x_coordinate_end = row + size
    elif heading == "right":
        if column + size >= grid_size:
            return False
        y_coordinate_end = column + size
    else:
        if column - size < 0:
            return False
        y_coordinate_start = column - size + 1

    # Having ensured the position is viable, its time to make one final check.
    return print_ship(y_coordinate_start, y_coordinate_end, x_coordinate_start, x_coordinate_end)    


def start_game():
    """
    The function that combines all the initial methods required to setup the game.
    Creates the grid and randomly places the ships.
    """
    # Global variables being modified inside this function.
    global grid_size
    global grid
    global ship_count
    global ship_location_storage

    # Using grid_size to set amount of columns and rows.
    columns = grid_size
    rows = grid_size

    grid = []
    for c in range(columns):
        column = []
        for r in range(rows):
            column.append(".")
        grid.append(column)

    # Here the random & time imports are utilized to ensure a random setup every game.
    random.seed(time.time())

    ships_made = 0
    ship_location_storage = []

    # While loop randomly finds ship size and position until ship_count is correct
    while ships_made != ship_count:
        pick_column = random.randint(0, columns - 1)
        pick_row = random.randint(0, rows - 1)
        ship_size = random.randint(2, 5)
        heading = random.choice(["up", "down", "right", "left"])
        if check_position(pick_column, pick_row, ship_size, heading):
            ship_size += 1


def make_grid():
    """
    Prints the grid to the terminal, to give the player a visual understanding of what's going on.
    """
    # Global variables being modified inside this function
    global grid
    global letters

    # Adjusting lenght of letters depending on chosen game lenght
    letters = letters[0: len(grid)+1]

    # for loop to print the grid (need to figure this out)




# Some user input to get the game started
