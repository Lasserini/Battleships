import random

"""
Import of random module to support building randomly placed ships later.

Legend for Grid:
"." = Water (empty space)
"#" = Ship (only used backend)
"X" = Hit (damaged ship)
"0" = Miss (water that has been shot at, without hitting a ship)

The program utilize a fair amount of global variables, they are listed below:
"""

# A variable for the grid upon which the ships are places
grid = [[]]

# Variable with letters, used to create the grid later.
letters = "ABCDEFGHIJ"

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

# Variable used to check if either game ending state is reached
game_complete = False


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
        grid_size = 6
        ship_count = 3
        shots_left = 18
    elif game_lenght == 2:
        grid_size = 8
        ship_count = 5
        shots_left = 32
    else:
        grid_size = 10
        ship_count = 8
        shots_left = 50
    return


def print_ship(
        y_coord_start, y_coord_end,
        x_coord_start, x_coord_end):
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
    for column in range(y_coord_start, y_coord_end):
        for row in range(x_coord_start, x_coord_end):
            if grid[column][row] != ".":
                empty_position = False
                break
    # If the coast is clear, we are ready to store the ships location
    if empty_position:
        ship_location_storage.append(
            [y_coord_start, y_coord_end,
                x_coord_start, x_coord_end])
        for column in range(y_coord_start, y_coord_end):
            for row in range(x_coord_start, x_coord_end):
                grid[column][row] = "#"
    return empty_position


def check_position(column, row, size, heading):
    """
    Function that uses the randomly generated ship info from setup_game.
    Combines the selected coordinate with lenght & heading to check if ship
        remains inside the grid.
    Calls support function that checks if the ship would collide with a
        previously placed ship.
    """
    # Global variables being modified inside this function
    global grid_size

    y_coord_start = column
    y_coord_end = column + 1
    x_coord_start = row
    x_coord_end = row + 1

    # Depending on which way the ship is heading we perform a different check.
    if heading == "up":
        if row - size < 0:
            return False
        x_coord_start = row - size + 1
    elif heading == "down":
        if row + size >= grid_size:
            return False
        x_coord_end = row + size
    elif heading == "right":
        if column + size >= grid_size:
            return False
        y_coord_end = column + size
    else:
        if column - size < 0:
            return False
        y_coord_start = column - size + 1

    # Having ensured the position is viable, its time to make one final check.
    return print_ship(
        y_coord_start, y_coord_end,
        x_coord_start, x_coord_end)


def setup_game():
    """
    The function that combines all the initial methods required to setup game.
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
    for x in range(rows):
        row = []
        for y in range(columns):
            row.append(".")
        grid.append(row)

    ships_made = 0
    ship_location_storage = []

    # While loop that keeps making ships till we have enough
    while ships_made != ship_count:
        pick_column = random.randint(0, columns - 1)
        pick_row = random.randint(0, rows - 1)
        ship_size = random.randint(2, 5)
        heading = random.choice(["up", "down", "right", "left"])
        if check_position(pick_column, pick_row, ship_size, heading):
            ships_made += 1


def make_grid():
    """
    Prints the grid to the terminal.
    Gives the player a visual understanding of what's going on.
    """
    # Global variables being modified inside this function
    global grid
    global letters

    # Adjusting lenght of letters depending on chosen game lenght
    letters = letters[0: len(grid)+1]

    # For loop to print the grid
    for row in range(len(grid)):
        print(letters[row], end=": ")
        for column in range(len(grid[row])):
            if grid[row][column] == "#":
                print(".", end=" ")
            else:
                print(grid[row][column], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")


def game_over():
    """
    A function that tests whether the game is won or lost.
    Enables the gameplay while loop in run_game() to end.
    """
    # Global variables being modified inside this function
    global ship_count
    global ships_sunk
    global shots_left
    global game_complete

    # Check whether the game is won or lost (REMEMBER TO UPDATE FLAVOURTEXT!)
    if shots_left <= 0:
        print("You lose")
        game_complete = True
    elif ship_count == ships_sunk:
        print("You won")
        game_complete = True


def where_to_shoot():
    """
    Function to prompt user for firing coordinates.
    A number of checks to ensure valid data input.
    """
    # Global variables being modified inside this function
    global letters
    global grid

    # Setting some variables to store user input etc.
    coord_correct = False
    row = -1
    column = -1
    while coord_correct is False:
        placement = input("Enter row and column fx D7: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Only enter one row and column such fx D7")
            continue
        row = placement[0]
        column = placement[1]
        if not row.isalpha() or not column.isnumeric():
            print("Error: Enter letter for row and number for column")
            continue
        row = letters.find(row)
        if not (-1 < row < grid_size):
            print("Error: Enter letter for row and number for column")
            continue
        column = int(column)
        if not (-1 < column < grid_size):
            print("Error: Enter letter for row and number for column")
            continue
        if grid[row][column] == "0" or grid[row][column] == "X":
            print("Location fired at previously. Try again")
            continue
        if grid[row][column] == "." or grid[row][column] == "#":
            coord_correct = True

    # sends the coordinates back to the fire() function
    return row, column


def ship_sunk(row, column):
    """
    Function that runs on a hit.
    Checks whether the entire ship is sunk.
    Needed to count ships_sunk, which is used to track game ending.
    """
    # Global variables being modified inside this function
    global ship_location_storage
    global grid

    # First we locate the ship in the ship storage variable
    for position in ship_location_storage:
        x_co_start = position[0]
        x_co_end = position[1]
        y_co_start = position[2]
        y_co_end = position[3]
        if x_co_start <= row <= x_co_end and y_co_start <= column <= y_co_end:
            # Then we check if the entire ship has been hit
            for r in range(x_co_start, x_co_end):
                for c in range(y_co_start, y_co_end):
                    if grid[r][c] != "X":
                        return False
    return True


def fire():
    """
    This function handles the steps taken when the user needs to fire a shoot.
    """
    # Global variables being modified inside this function
    global grid
    global shots_left
    global ships_sunk

    # Using where_to_shoot to get coordinates returned in a tuple
    row, column = where_to_shoot()
    print("")
    print("----------------------------")

    # Checking what the shot hit & applying consequence
    if grid[row][column] == ".":
        print("You hear a large 'blop' as your MISS! hits the water")
        grid[row][column] = "0"
    elif grid[row][column] == "#":
        print("KABOOM! An amazing HIT", end=" ")
        grid[row][column] = "X"
        if ship_sunk(row, column):
            print("Success! The ship takes a massive blow and sinks!")
            ships_sunk += 1
        else:
            print("That ship needs another HIT!")

    # Updates the counter for remaining ammunition
    shots_left -= 1


def run_game():
    """
    Function to start the game upon loading the program.
    Provides some welcome text to the user.
    It checks whether game_complete state is reached.
    """
    # Global variables being modified inside this function
    global game_complete

    print("Welcome to Battleship Commander")
    print("Can you sink all the enemy ships before it's too late?")

    # Calling the function that randomly generates the gameboard
    setup_game()

    # The while loop that is essentially the gameplay loop
    while game_complete is False:
        make_grid()
        print("Ammunition left: " + str(shots_left))
        print(str(ship_count-ships_sunk) + " enemy ships incoming!")
        # Calling shoot() which handles anything related to fireing shoots
        fire()
        # & finally calling the function changes game_complete when required
        game_over()


def set_difficulty():
    """
    Function that prompts user for desired difficulty.
    """
    # Global variables being modified inside this function
    global game_lenght

    game_lenght = int(input("Select game lenght, Short=1, Medium=2, Long=3: "))


def welcome():
    """
    Displays a welcome flavourtext message.
    Asks user to select game length.
    Calls the run_game function to start gameplay loop.
    """
    # Global variables being modified inside this function
    global game_lenght

    print("Welcome to Battleship Commander")
    print("Can you sink all the enemy ships before it's too late?")
    print("- - -")
    print("Rules")
    print("Based upon your chosen lenght, the game creates a board")
    print("The board has hidden ships, ranging from size 2-5")
    print("Inform the ships cannoneer which quadron to aim for")
    print("Legend")
    print(". is water, X represents a Hit!, 0 a Miss")
    print("- - -")
    print("Sink all the ships before ammunition runs out")
    print("Good luck!")
    print("- - -")

    # Asking the user to set game lenght
    set_difficulty()

    # Calling the function that initiates the gameplay loop.
    if 1 <= game_lenght <= 3:
        difficulty_setting(game_lenght)
        run_game()
    else:
        print("Error: Type a number between 1 & 3 to select game lenght")
        set_difficulty()


# The function above is called, providing a welcome message.
welcome()
