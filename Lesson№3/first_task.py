# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
user_sentence = input("Введите ваше предложение: ")
split_method = user_sentence.split(' ')
join_method = '-'.join(split_method)
print(join_method)

replace_method = user_sentence.replace(' ', '-')
print(replace_method)
