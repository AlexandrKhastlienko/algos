# Реализуйте алгоритм бинарного поиска, который ищет значение `key` в отсортированном списке `numbers_list`.
# Выведите на экран следующую информацию:
# "True" — если элемент найден, "False" — если не найден.
# Количество сравнений с серединным элементом, которые были совершены, чтобы завершить бинарный поиск.

numbers_list = [0, 20, 30, 34, 45, 56, 67, 78, 90, 100, 110]

sorted_number_list = sorted(numbers_list)

left = 0
right = len(sorted_number_list) - 1
middle = 0
key = 100
cnt = 0

while left <= right:
    middle = (left + right) // 2

    if key > sorted_number_list[middle]:
        left = middle + 1
        cnt += 1
    elif key < sorted_number_list[middle]:
        right = middle - 1
        cnt += 1
    elif key == sorted_number_list[middle]:
        print("True", cnt + 1)
        break

if key != sorted_number_list[middle]:
    print('False', cnt)
