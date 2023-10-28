def find_common_participants(str1_, str2_, separator=','):
    first_list = str1_.split(separator)
    second_list = str2_.split(separator)
    participants = list(set(first_list).intersection(second_list))
    participants.sort()
    return participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, '|')
print("Список общих участников: ", common_participants)
