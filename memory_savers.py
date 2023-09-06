# functia LAMBDA

# my_lambda = lambda x, y: x + y
#
# print(my_lambda(5, 3))

players = [
    {
    'first_name': 'John',
    'last_name': 'Doe',
    'rank': 5
    },
    {
    'first_name': 'Kevin',
    'last_name': 'McDonald',
    'rank': 1
    },
    {
    'first_name': 'Brad',
    'last_name': 'Kelvin',
    'rank': 2
    }
]

# print(players)
# sorted_players = sorted(players, key=lambda player : player['rank'], reverse=False)
# # sorted_players = sorted(players, key=lambda player : player['rank'], reverse=True)
#
# print(sorted_players)

# functii MAP
#AAA

# def check_top_3_player(player):
#     updated_player = dict(player)
#     updated_player['is top 3'] = True if updated_player['rank'] <=3 else False
#     return updated_player
#
# print(check_top_3_player(players[0]))

#BBB

# def check_top_3_player(player):
#     updated_player = dict(player)
#     updated_player['is top 3'] = True if updated_player['rank'] <=3 else False
#     return updated_player
#
# top_3_players = map(check_top_3_player, players)
# print(list(top_3_players))

#functii FILTER
all_mcdonalds = list(filter(lambda player: True if player['last_name'] == 'McDonald' else False, players))
print(all_mcdonalds)


#functii ZIP
letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4, 5, 6, 7]
for zip_item in zip(letters, numbers):
    print(zip_item)
