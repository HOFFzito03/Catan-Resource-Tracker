def distribute_starting_resources(players_names, player_settlements, players_resources):

#Starting resource distribution
    for player in players_names:
        for hex in player_settlements[player]["settlement_2"]:
         resource = hex["resource"]
         players_resources[player][resource] += 1

#Resource overview
def resource_overview(players_resources):
    print("\nResource Overview:")
    for player in players_resources:
        total_resources = 0
        print(f"\n{player}")

        for resource, amount in players_resources[player].items():
            print(resource, amount)
            total_resources += amount

        print(f"Total resources: {total_resources}")