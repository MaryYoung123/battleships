from random import randrange

ship_initial = ["B", "C", "F", "A", "S"]
ship_names = ["Battleship", "Cruiser", "Frigate", "Aircraft Carrier", "Sub"]
map_size = 10

def get_username():
    """
    To ask user to input their name
    """
    while True:
        user_name = input("Please enter your name, comrade!: ")
        if user_name:
            print(f"Welcome to battleships, {user_name}!")
            return user_name
        else:
            print("Please enter your name!")


def create_battlefield(map_size):
    """
    function to create the battlefield size
    """
    return [["_"] * map_size for _ in range(map_size)]

def display_battlefield(board):
    """
    function to display current state of the map.
    """
    for row in board:
        print(" ".join(row))

def player_coordinate(player_board, occupied):
    """
    function for player placement of ship
    """
    while True:
        try:
            row = int(input("Enter the row for Battleship: "))
            col = int(input("Enter the column for Battleship: "))
            if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                player_board[row][col] = "B"
                occupied.add((row, col))
                break
            else:
                print("Invalid coordinates. Please enter correct value.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            row = int(input("Enter the row for Cruiser: "))
            col = int(input("Enter the column for Cruiser: "))
            if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                player_board[row][col] = "C"
                occupied.add((row, col))
                break
            else:
                print("Invalid coordinates. Please enter correct values.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            row = int(input("Enter the row for Frigate: "))
            col = int(input("Enter the column for Frigate: "))
            if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                player_board[row][col] = "F"
                occupied.add((row, col))
                break
            else:
                print("Invalid coordinates. Please enter correct values")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            row = int(input("Enter the row for Aircraft Carrier: "))
            col = int(input("Enter the column for Aircraft Carrier: "))

            if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                player_board[row][col] = "A"
                occupied.add((row, col))
                break
            else:
                print("Invalid coordinates. Please enter correct values")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            row = int(input("Enter the row for Submarine: "))
            col = int(input("Enter the column for Submarine: "))

            if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                player_board[row][col] = "S"
                occupied.add((row, col))
                break
            else:
                print("Invalid coordinates. Please enter correct values")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return player_board, occupied

def comp_coordinate(comp_board):
    """
    function for computer opponent.
    """
    for ship in ship_initial:
        while True:
            row = randrange(0, 10)
            col = randrange(0, 10)
            if comp_board[row][col] == "_":
                comp_board[row][col] = ship
                break

    return comp_board

def check_player_hit(comp_board, dummy_board, user):
    """
    Function for player hit or miss
    """
    print(user)
    row = int(input("Enter your row: "))
    col = int(input("Enter your col: "))
    hit = 1

    if comp_board[row][col] == "B":
        comp_board[row][col] = "b"
        dummy_board[row][col] = "X"
        print("Computer: Battleship been hit!")
    elif comp_board[row][col] == "C":
        comp_board[row][col] = "c"
        dummy_board[row][col] = "X"
        print("Computer: Cruiser been hit!")
    elif comp_board[row][col] == "F":
        comp_board[row][col] = "f"
        dummy_board[row][col] = "X"
        print("Computer: Frigate been hit!")
    elif comp_board[row][col] == "A":
        comp_board[row][col] = "a"
        dummy_board[row][col] = "X"
        print("Computer: Aircraft Carrier been hit!")
    elif comp_board[row][col] == "S":
        comp_board[row][col] = "s"
        dummy_board[row][col] = "X"
        print("Computer: Sub been hit!")
    else:
        dummy_board[row][col] = "*"
        hit = 0 
        print("Missed me!")

    return hit