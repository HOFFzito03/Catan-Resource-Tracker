#Purchase function
def purchase(player, item, building_costs, players_resources):

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