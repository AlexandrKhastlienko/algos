# посчитать кол-во чётных элементов

week_data = [1, 20, 12, 35, 0, 7, 8]

even_day_id = []

for i in range(len(week_data)):
    if week_data[i] % 2 == 0:
        even_day_id.append(i + 1)

print(even_day_id)
