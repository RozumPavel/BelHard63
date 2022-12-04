# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

dict1 = {"name": input("Введите ваше имя: "), "email": input("Введите вашу почту: ")}
dict2 = {i: dict1 for i in "0"}

dict3 = {"name": input("Введите ваше имя: "), "email": input("Введите вашу почту: ")}
dict4 = {i: dict3 for i in "1"}

general_dict = dict2 | dict4
print(general_dict)
