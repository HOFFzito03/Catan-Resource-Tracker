import json

from game.setup import setup_settlements, load_game_setup
from game.resources import distribute_starting_resources, resource_overview
from game.buildings import purchase

print("Welcome to Catan Resource Tracker!")

#Player registration
players_names = ["Jonas", "Aksel", "Mikkel", "Andreas"]

#Resource dictionary
players_resources = {}

for player in players_names:
    players_resources[player] = {
        "wood": 0,
        "brick": 0,
        "sheep": 0,
        "wheat": 0,
        "ore": 0
    }

#Building costs dictionary
building_costs = {
    "road": {
        "wood": 1,
        "brick": 1
    },
    "settlement": {
        "wood": 1,
        "brick": 1,
        "sheep": 1,
        "wheat": 1
    },
    "city": {
        "wheat": 2,
        "ore": 3
    },
    "development_card": {
        "sheep": 1,
        "wheat": 1,
        "ore": 1
    }
}

#Start menu
while True:
    print("\nWelcome to Catan Resource Tracker!")
    print("1. New Game")
    print("2. Load Game")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        print("\nStarting a new game...")
        player_settlements = setup_settlements(players_names)
        break

    elif choice == "2":
        try:
            player_settlements = load_game_setup()

            print("\nGame setup loaded successfully!")
            break

        except FileNotFoundError:
            print("\nNo saved game setup found. Please start a new game.")

    elif choice == "3":
        print("\nGoodbye!")
        raise SystemExit

    else:
        print("\nInvalid choice. Please choose 1, 2 or 3.")

#Game loop
game_running = True

round_counter = 1

while game_running:
    print(f"\n--- Round {round_counter} ---")
    # Dice roll registration
    dice_rolls = input("\nEnter the dice rolls: ")

    if dice_rolls == "q":
        break

    dice_rolls = int(dice_rolls)

    #Resource distribution
    for player in player_settlements:
        for settlement in player_settlements[player].values():
                for hex in settlement:
                    if hex["number"] == dice_rolls:
                        resource = hex["resource"]
                        players_resources[player][resource] += 1

    #Resource overview
    resource_overview(players_resources)
    round_counter += 1