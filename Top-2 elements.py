# Есть список с транзакциями клиентов.
#
# Вам нужно отсортировать этот список таким образом, чтобы две максимальные транзакции,
# отсортированные по возрастанию, оказались в конце списка.
#
# Порядок остальных элементов значения не имеет.
# Для решения этой задачи доработайте алгоритм сортировки пузырьком.



transactions = [100, 98, 1000, 2500, 299, 1898, 1989, 2001, 50, 10, 70]

for i in range(len(transactions) - 1):
    for j in range(len(transactions)-i-1):
        if  transactions[j] > transactions[-1]:
            transactions[j], transactions[-1] = transactions[-1], transactions[j]
        elif  transactions[j] > transactions[-2]:
            transactions[j], transactions[-2] = transactions[-2], transactions[j]

print(transactions)