# Creates a blank grid for the game to start/restart
def blankGrid(grid):
    for row in range(3):
        grid.append(["*"] * 3)


# Creates a visual grid for the players to understand
def displayGrid(player1, player2, grid):
    counter = 1
    for row in range(3):
        for column in range(3):
            if (grid[row][column] != player1) and (grid[row][column] != player2):
                grid[row][column] = str(counter)
            counter += 1
    printGrid(grid)


# Prints the current state of the grid
def printGrid(grid):
    for row in grid:
        print" | ".join(row)
    print ""


#Places a players piece in the desired location
def placeGrid(player1, player2, turn, grid):
    check = False
    displayGrid(player1, player2, grid)
    if turn:
        input = raw_input("Player 1, where would you like to put your piece? ")
    if not turn:
        input = raw_input("Player 2, where would you like to put your piece? ")

    for row in range(3):
        for column in range(3):
            if (grid[row][column] == str(input)) and (turn):
                grid[row][column] = player1
                check = True
            elif (grid[row][column] == str(input)) and (not turn):
                grid[row][column] = player2
                check = True
    return check


# Checks if a player has won
def checkWin(grid, player1, player2, turn):
    check = False
    if turn:
        if (((grid[0][0] == player1) and (grid[0][1] == player1) and (grid[0][2] == player1)) or
           ((grid[1][0] == player1) and (grid[1][1] == player1) and (grid[1][2] == player1)) or
           ((grid[2][0] == player1) and (grid[2][1] == player1) and (grid[2][2] == player1)) or
           ((grid[0][0] == player1) and (grid[1][0] == player1) and (grid[2][0] == player1)) or
           ((grid[0][1] == player1) and (grid[1][1] == player1) and (grid[2][1] == player1)) or
           ((grid[0][2] == player1) and (grid[1][2] == player1) and (grid[2][2] == player1)) or
           ((grid[0][0] == player1) and (grid[1][1] == player1) and (grid[2][2] == player1)) or
           ((grid[0][2] == player1) and (grid[1][1] == player1) and (grid[2][0] == player1))):
            check = True
            print "Player 1 wins!"

    elif not turn:
        if (((grid[0][0] == player2) and (grid[0][1] == player2) and (grid[0][2] == player2)) or
           ((grid[1][0] == player2) and (grid[1][1] == player2) and (grid[1][2] == player2)) or
           ((grid[2][0] == player2) and (grid[2][1] == player2) and (grid[2][2] == player2)) or
           ((grid[0][0] == player2) and (grid[1][0] == player2) and (grid[2][0] == player2)) or
           ((grid[0][1] == player2) and (grid[1][1] == player2) and (grid[2][1] == player2)) or
           ((grid[0][2] == player2) and (grid[1][2] == player2) and (grid[2][2] == player2)) or
           ((grid[0][0] == player2) and (grid[1][1] == player2) and (grid[2][2] == player2)) or
           ((grid[0][2] == player2) and (grid[1][1] == player2) and (grid[2][0] == player2))):
            check = True
            print "Player 2 wins!"

    return check


# Checks if the match is a draw
def checkDraw(grid):
    check = True
    counter = 1
    for row in range(3):
        for column in range(3):
            if grid[row][column] == str(counter):
                check = False
            counter += 1
    return check


# Checks if all the positions in the grid are filled up
def checkDone(grid, player1, player2, turn):
    check = False
    if checkWin(grid, player1, player2, turn):
        check = True
    elif checkDraw(grid):
        print "It's a draw!"
        check = True

    return check

# The main function (It's a Java thing I know but I'm so used to it)
print "Welcome to Tic Tac Toe! **Python Edition**"

game = True
while game:
    turn = False
    grid = []
    player1 = ""
    player2 = ""
    blankGrid(grid)
    printGrid(grid)
    check = False
    while not check:
        input = raw_input("Player 1 do you want to be X's or O's? ")
        if input.lower() == "X".lower():
            player1 = "X"
            player2 = "O"
            check = True
        elif input.lower() == "O".lower():
            player1 = "O"
            player2 = "X"
            check = True
        else:
            print "\nInvalid Input!"
    while game:
        if turn:
            turn = False
            while not placeGrid(player1, player2, turn, grid):
                print "\nInvalid Place!"
        else:
            turn = True
            while not placeGrid(player1, player2, turn, grid):
                print "\nInvalid Place!"
        if checkDone(grid, player1, player2, turn):
                    game = False
                    printGrid(grid)
    print "Game Over!\n"
    check = False
    while not check:
        input = raw_input("Would you like to play again, Yes/No? ")
        if input.lower() == "yes".lower():
            game = True
            print "\nYay! Let's Go...\n"
            check = True
        elif input.lower() == "no".lower():
            game = False
            print "\nAwhh! Maybe Next Time..."
            check = True
        else:
            print "\nInvalid Input!"
