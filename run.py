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