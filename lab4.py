import random

SIZE = 5

# Создание и заполнение массива
matrix = []

for i in range(SIZE):
    row = []
    for j in range(SIZE):
        row.append(random.randint(10, 99))
    matrix.append(row)

print("Исходный массив:")

for row in matrix:
    print(*row)

# Поиск максимального элемента в каждой строке
# и обмен его с первым элементом
for i in range(SIZE):
    max_index = 0

    for j in range(1, SIZE):
        if matrix[i][j] > matrix[i][max_index]:
            max_index = j

    matrix[i][0], matrix[i][max_index] = \
        matrix[i][max_index], matrix[i][0]

print()
print("Массив после замены максимальных элементов:")

for row in matrix:
    print(*row)