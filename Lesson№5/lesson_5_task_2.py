# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число
first_number = input("Введите первое число: ")
action = input("Введите необходимое действие: ")
second_number = input("Введите второе число: ")
correct_actions_list = ["плюс", "сумма",  "минус", "разница", "разделить", "деление", "умножить", "умножение", 
"степень", "возвести в степень", "разделить по модулю", "деление по модулю", "деление с остатком", "целочисленное деление"]

while not first_number.isdigit():
    first_number = input("Введите первое число: ")
while action not in correct_actions_list:
    action = input("Введите корректное действие: ")
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
