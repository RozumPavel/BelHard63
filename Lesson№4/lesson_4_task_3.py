# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

user_name = input("Введите ваше имя: ")
user_email = input("Введите вашу почту: ")
user_name1 = input("Введите ваше имя: ")
user_email1 = input("Введите вашу почту: ")

dict1 = {"name": user_name, "email": user_email}
dict2 = {i: dict1 for i in "0"}

dict3 = {"name": user_name1, "email": user_email1}
dict4 = {i: dict3 for i in "1"}

general_dict = dict2 | dict4
print(general_dict)
