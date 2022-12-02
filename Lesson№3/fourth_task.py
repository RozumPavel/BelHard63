# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
# Первый способ
first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
third_number = float(input("Введите третье число: "))
if first_number >= 1 and second_number >= 1 and third_number >= 1:
    print("Все три числа являются положительными")

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

answer_positive_number = sum([first_number, second_number, third_number])
print("Количество положительных чисел из трех введенных: ", answer_positive_number)

answer_negativ_number = 3 - answer_positive_number
print("Количество отриицательных чисел (или нулей) из трех введенных: ", answer_negativ_number)

# Второй способ
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
negative_count = 0
negative_count += (a >> 31) & 1
negative_count += (b >> 31) & 1
negative_count += (c >> 31) & 1
positive_count = 3 - negative_count
negative_count
print("Количество положительных чисел", positive_count)
print("Количество отрицательных чисел", negative_count)

# Третий способ
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))
first_number_bool_positive = bool(first_number > 0)
second_number_bool_positive = bool(second_number > 0)
third_number_bool_positive = bool(third_number > 0)
sum_numbers_positive = int(first_number_bool_positive + second_number_bool_positive + third_number_bool_positive)
print("Количество положительных чисел из трех введенных:", sum_numbers_positive)

first_number_bool_negative = bool(first_number <= 0)
second_number_bool_negative = bool(second_number <= 0)
third_number_bool_negative = bool(third_number <= 0)
sum_numbers_negative = int(first_number_bool_negative + second_number_bool_negative + third_number_bool_negative)
print("Количество отрицательных чисел (или нулей) из трех введенных:", sum_numbers_negative)
