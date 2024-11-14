# Дан список `week_data` из семи элементов, который хранит в себе количество обращений,
# обработанных кол-центром в каждый день недели. Выведите первый порядковый номер дня,
# в который было обработано меньше всего обращений.

week_data = [1, 20, 12, 35, 0, 7, 8]

day_min = week_data[0]
day_min_id = 0

for i in range(len(week_data)):
    if day_min > week_data[i]:
        day_min = week_data[i]
        day_min_id = i

print(day_min_id + 1)