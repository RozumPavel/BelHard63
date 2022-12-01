# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
response = input("Введите ваше предложение: ")
split_method = response.split(' ')
join_method = '-'.join(split_method)
print(join_method)


response1 = input("Введите ваше предложение: ")
replace_method = response1.replace(' ', '-')
print(replace_method)


# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3
x = float(input("Введи первое число: "))
y = float(input("Введи второе число: "))
z = float(input("Введи третье число: "))
three_sums = (x, y, z)
general_sum = sum(three_sums)
pre_answer = general_sum/3
answer = round(pre_answer, 3)
print(answer)