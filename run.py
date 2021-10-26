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
"#" = Ship (undamaged)
"X" = Hit (damaged ship)
"0" = Miss (water that has been shot at, without hitting a ship)
"""

# Imports used to generate random ship placement, time to help ensure randomness.
    # random.seed(time.time()) -> makes the random seed time dependant, to ensure new random seed for additional games. Used in create_grid.
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

