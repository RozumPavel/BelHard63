# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
response = input("Введите ваше предложение: ")
split_method = response.split(' ')
join_method = '-'.join(split_method)
print(join_method)


response1 = input("Введите ваше предложение: ")
replace_method = response1.replace(' ', '-')
print(replace_method)
