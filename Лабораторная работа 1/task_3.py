list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count_players = len(list_players)
half_players = count_players // 2
first_team = list_players[:half_players]
second_team = list_players[half_players:]

print(first_team)
print(second_team)