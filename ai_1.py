import numpy as np

# 1

# Створіть масив:
# [1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16]

array_1 = np.array(range(1, 17))
array_1 = array_1.reshape(4, 4)

# Використовуючи індекси виведіть:

fourteen = array_1[3, 1] # число 14
print(fourteen)

third_raw = array_1[2,] # третій рядок
print(third_raw)

first_column = array_1[:, 0] #  перший стовпчик
print(first_column)

upper_half = array_1[:2, ] # верхню половину
print(upper_half)

array_1[1:3, ] = 100 # замініть числа в рядках 2-3 на 100
print(array_1)

array_1[1, ] = array_1[3, ] #  зробіть другий рядок таким як останній рядок
print(array_1)

# 2

# У масиві з попереднього завдання створіть маску для
# парних чисел. З її допомогою
# виведіть самі числа

even_nums = array_1 % 2 == 0
print(array_1[even_nums])

# замініть їх на 100

array_1[even_nums] = 100

# 3

# Створіть 2 масиви типу uint8:
# Масив 1: 128 200 10
# Масив 2: 250 10 34

array2 = np.array([128, 200, 10], dtype=np.uint8)
array3 = np.array([250, 10, 34], dtype=np.uint8)

# Об’єднайте їх у пропорції 20% першого масиву + 80%
# другого масиву. В результаті має бути тип даних uint8 та
# числа в діапазоні 0-255

array_concat = (0.2 * array2 + 0.8 * array3).astype(np.uint8)