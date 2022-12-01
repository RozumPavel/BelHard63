# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
first_number = float(input("Введи первое число: "))
second_number = float(input("Введи второе число: "))
third_number = float(input("Введи третье число: "))
if first_number >= 1 and second_number >= 1 and third_number >= 1:
    print("Все три числа являются положительными")
else:
    print("Не все из введеных трех чисел являются положительными")
if first_number >= 1:
    print("Первое число является положительным")
else:
    print("Первое число является отрицательным или нулем")
if second_number >= 1:
    print("Второе число является положительным")
else:
    print("Второе число является отрицательным или нулем")
if third_number >= 1:
    print("Третье число является положительным")
else:
    print("Третье число является отрицательным или нулем")
if first_number <= 0 and second_number <= 0 and third_number <= 0:
    print("Все три числа являются отрицательными")

if first_number >= 1:
    first_number = 1
else:
    first_number = 0

if second_number >= 1:
    second_number = 1
else:
    second_number = 0

if third_number >= 1:
    third_number = 1
else:
    third_number = 0

answer = float(first_number + second_number + third_number)
print("Количество положительных чисел: ", answer)
