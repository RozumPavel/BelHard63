# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
# Сделал 4 (конкатенация, %форматирование, format, f_string)
name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
city = input("Введите ваш город: ")
answer = name + ' ' + age + ' ' + city
print("Приветствую," + ' ' + answer)

name_feedback = name
age_feedback = age
city_feedback = city
answer2 = f"Приветствую, {name_feedback} {age_feedback} {city_feedback}"
print(answer2)
