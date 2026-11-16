import json

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

#Settlement registration
def setup_settlements():
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


#Run settlement registration
player_settlements = setup_settlements()


#Starting resource distribution
for player in players_names:
    for hex in player_settlements[player]["settlement_2"]:
        resource = hex["resource"]
        players_resources[player][resource] += 1


#Resource overview
def resource_overview():
    print("\nResource Overview:")
    for player in players_resources:
        total_resources = 0
        print(f"\n{player}")

        for resource, amount in players_resources[player].items():
            print(resource, amount)
            total_resources += amount

        print(f"Total resources: {total_resources}")

#Purchase function
def purchase(player, item):

    costs = building_costs[item]

     #Check if player can afford the purchase
    for resource, amount in costs.items():

        if players_resources[player][resource] < amount:

            print(f"Not enough {resource}!")

            return False

    #Deduct resources
    for resource, amount in costs.items():
        players_resources[player][resource] -= amount

    print(f"{player} purchased {item}!")
    return True

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
        for settlement in player_settlements[player]:
            if settlement["number"] == dice_rolls:
                resource = settlement["resource"]
                players_resources[player][resource] += 1

    #Resource overview
    resource_overview()
    round_counter += 1