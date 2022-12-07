# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число
first_number = input("Введите первое число: ")
action = input("Введите необходимое действие: ")
second_number = input("Введите второе число: ")

while not first_number.isdigit():
    first_number = input("Введите первое число: ")
while not action.isalpha():
    action = input("Введите необходимое действие: ")
while not second_number.isdigit():
    second_number = input("Введите второе число: ")


if action == "плюс" or action == "сумма":
    print(float(first_number) + float(second_number))
elif action == "минус" or action == "разница":
    print(float(first_number) - float(second_number))
elif action == "разделить" or action == "деление":
    print(float(first_number) / float(second_number))
elif action == "умножить" or action == "умножение":
    print(float(first_number) * float(second_number))
elif action == "степень" or action == "возвести в степень":
    print(float(first_number) ** float(second_number))
elif action == "разделить по модулю" or action == "деление по модулю" or action == "деление с остатком":
    print(float(first_number) % float(second_number))
elif action == "целочисленное деление":
    print(float(first_number) // float(second_number))
else:
    print("Введено неверное действие")
