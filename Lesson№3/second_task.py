# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3
first_number = float(input("Введи первое число: "))
second_number = float(input("Введи второе число: "))
third_number = float(input("Введи третье число: "))
three_sums = (first_number, second_number, third_number)
general_sum = sum(three_sums)
pre_answer = general_sum/3
answer = round(pre_answer, 3)
print(answer)
