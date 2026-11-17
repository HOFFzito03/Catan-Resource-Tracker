#Settlement registration
import json

def setup_settlements(players_names):
    player_settlements = {}

    for player in players_names:
        player_settlements[player] = {
            "settlement_1": [],
            "settlement_2": []
        }

    #First settlement round
    for player in players_names:
        print(f"\nRegister Settlement 1 for {player}")

        while True:
            resource = input("Enter resource (or 'done'): ").lower()

            if resource == "done":
                break

            if resource not in ["wood", "brick", "sheep", "wheat", "ore"]:
                print("Invalid resource. Try again.")
                continue

            number = int(input("Enter hex number: "))

            if number < 2 or number > 12:
                print("Invalid number. Enter a number between 2 and 12.")
                continue

            player_settlements[player]["settlement_1"].append({
                "resource": resource,
                "number": number
            })

    #Second settlement round - reverse order
    for player in reversed(players_names):
        print(f"\nRegister Settlement 2 for {player}")

        while True:
            resource = input("Enter resource (or 'done'): ").lower()

            if resource == "done":
                break

            if resource not in ["wood", "brick", "sheep", "wheat", "ore"]:
                print("Invalid resource. Try again.")
                continue

            number = int(input("Enter hex number: "))

            if number < 2 or number > 12:
                print("Invalid number. Enter a number between 2 and 12.")
                continue

            player_settlements[player]["settlement_2"].append({
                "resource": resource,
                "number": number
            })

    #Save game setup to JSON file
    with open("data/game_setup.json", "w") as file:
        json.dump(player_settlements, file, indent=4)

    return player_settlements

def load_game_setup():
    with open("data/game_setup.json", "r") as file:
        return json.load(file)