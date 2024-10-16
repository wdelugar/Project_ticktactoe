from art import *


def main():
    tprint("TIC TAC TOE", font="random")
    print("Welcome players!")
    print("Choose your weapon between X and O. "
          "First to make three of their marks in a horizontal, vertical, or diagonal row wins the game.")
    input("Press enter to continue.")
    print("\n")

    board = create_grid()
    print_pretty(board)
    player_1, player_2 = weapon()
    # starts the game
    isFull(board, player_1, player_2)


def create_grid():
    # creates a blank playboard
    print("Here is your arena: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board


def weapon():
    # Player to chose weapon (X or O)
    weapon_choice = False
    player_1 = ""
    while not weapon_choice:
        player_1 = input("Player 1 choose between X and O. ")
        weapon_choice = invalid_weapon(player_1)

    if player_1.upper() == "X":
        player_2 = "O"
        print("Player 2, you are O. ")
    else:
        player_2 = "X"
        print("Player 2, you are X. ")
    input("Press enter to continue.")
    print("\n")
    return player_1.upper(), player_2.upper()


def invalid_weapon(player_1):
    if player_1.upper() != "O" and player_1.upper() != "X":
        print("Invalid choice of weapon.")
        return False
    return True


def start_game(board, player_1, player_2, count):
    # Game starts.
    if count % 2 == 0:
        player = player_1
    elif count % 2 == 1:
        player = player_2
    print("Player " + player + ", it is your turn. ")

    # check for valid inputs
    valid_input = False
    row = 0
    column = 0
    while not valid_input:
        row = input("Pick a row number: ")
        column = input("Pick a column number: ")
        valid_input = check_input(board, row, column, player_1, player_2)

        # Assign player on the board
    if player == player_1:
        board[int(row)][int(column)] = player_1

    else:
        board[int(row)][int(column)] = player_2

    return board


def isFull(board, player_1, player_2):
    count = 1
    winner = True
    # This function check if the board is full
    while count < 10 and winner == True:
        start_game(board, player_1, player_2, count)
        print_pretty(board)

        if count == 9:
            print("Game over.")
            print("It is a tie! ")

        # Check for winner
        winner = isWinner(board, player_1, player_2, count)
        count += 1

    if not winner:
        print("Game over.")


def check_input(board, row, column, player_1, player_2):
    # Position is out of range
    if not row.isnumeric() or not column.isnumeric():
        print(f"Invalid position {row, column}. Pick another one. ")
        return False
    # Check if players' selection is out of range
    elif (int(row) > 2 or int(row) < 0) or (int(column) > 2 or int(column) < 0):
        print(f"Invalid position {row, column}. Pick another one. ")
        return False
    # Check if the square is already filled
    elif (board[int(row)][int(column)] == player_1) or (board[int(row)][int(column)] == player_2):
        print(f"Position {int(row), int(column)}  already taken. Pick another one.")
        return False
    return True


def print_pretty(board):
    # This function prints the board

    rows = len(board)
    cols = len(board)
    print("    0   1   2 ")
    print("   ---+---+---")
    for r in range(rows):
        print(r, " ", board[r][0], "|", board[r][1], "|", board[r][2])
        print("   ---+---+---")
    return board


def isWinner(board, player_1, player_2, count):
    # Checks for winners
    winner = True
    # Check the rows
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == player_1):
            winner = False
            print("Player " + player_1 + ", you win!")

        elif (board[row][0] == board[row][1] == board[row][2] == player_2):
            winner = False
            print("Player " + player_2 + ", you win!")

    # Check the columns
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == player_1):
            winner = False
            print("Player " + player_1 + ", you win!")
        elif (board[0][col] == board[1][col] == board[2][col] == player_2):
            winner = False
            print("Player " + player_2 + ", you win!")

    # Check the diagonals
    if board[0][0] == board[1][1] == board[2][2] == player_1:
        winner = False
        print("Player " + player_1 + ", you win!")

    elif board[0][0] == board[1][1] == board[2][2] == player_2:
        winner = False
        print("Player " + player_2 + ", you win!")

    elif board[0][2] == board[1][1] == board[2][0] == player_1:
        winner = False
        print("Player " + player_1 + ", you win!")

    elif board[0][2] == board[1][1] == board[2][0] == player_2:
        winner = False
        print("Player " + player_2 + ", you win!")

    return winner


# Call Main
main()
