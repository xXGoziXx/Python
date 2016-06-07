from random import randint


def print_board(board):
    for row in board:
        print " ".join(row)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


def ships_sunk(board):
    counter = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "*":
                counter += 1
    return counter


print "Welcome to Battleship! **Python Edition**"
print ""
print "Let's play Battleship!"
game = True
while game:
    board = []
    for x in range(5):
        board.append(["O"] * 5)

    ship = []
    ship1 = []
    ship2 = []
    ship.append(random_row(board))
    ship.append(random_col(board))
    ship1.append(random_row(board))
    ship1.append(random_col(board))
    ship2.append(random_row(board))
    ship2.append(random_col(board))
    print_board(board)

    while (((ship[0] == ship1[0]) and (ship[1] == ship1[1])) or ((ship[0] == ship2[0]) and (ship[1] == ship2[1]))):
        ship[0] = random_row(board)
        ship[1] = random_col(board)
        while (((ship1[0] == ship2[0]) and (ship1[1] == ship2[1]))):
            ship1[0] = random_row(board)
            ship1[1] = random_col(board)
    turn = 5
    counter = turn
    while turn < (counter * 2):
        print ""
        guess_row = int(raw_input("Guess Row: "))
        guess_col = int(raw_input("Guess Col: "))
        guess_row -= 1
        guess_col -= 1
        if ((guess_row == ship[0]) and (guess_col == ship[1])) or ((guess_row == ship1[0]) and (guess_col == ship1[1])) or ((guess_row == ship2[0]) and (guess_col == ship2[1])):
            print "Congratulations! You sunk my battleship!"
            board[guess_row][guess_col] = "*"
            turn += 1
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, that's not even in the ocean. Try Again!"
            elif (board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
                turn += 1
        print turn - counter
        print_board(board)
    print "Ships sunk: " + str(ships_sunk(board))
    print "Game Over!"
    input = str(raw_input("\nWould you like to play again? YES/NO\n"))
    if input.lower() == "yes":
        print "\nOk! Starting new game...\n"
    elif input.lower() == "no":
        print "Ok! Finished."
