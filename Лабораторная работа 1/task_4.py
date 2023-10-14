users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
users_dict = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
count_users = len(users)
count_unique_users = len(set(users))
users_dict["Общее количество"] = count_users
users_dict["Уникальные посещения"] = count_unique_users

print(users_dict)