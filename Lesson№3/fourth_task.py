# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
first_number = float(input("Введи первое число: "))
second_number = float(input("Введи второе число: "))
third_number = float(input("Введи третье число: "))
if first_number and second_number and third_number >= 1:
    print("Все три числа являются положительными")
else:
    print("Не все числа из списка являются положительными")
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
