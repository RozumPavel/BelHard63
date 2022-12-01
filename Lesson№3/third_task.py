# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
# Сделал 4 (конкатенация, %форматирование, format, f_string)
name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
city = input("Введите ваш город: ")
answer = name + ' ' + age + ' ' + city
print("Приветствую," + ' ' + answer)

name1 = input("Введите ваше имя: ")
age1 = input("Введите ваш возраст: ")
city1 = input("Введите ваш город: ")
name_feedback = name1
age_feedback = age1
city_feedback = city1
answer2 = f"Приветствую, {name_feedback} {age_feedback} {city_feedback}"
print(answer2)
