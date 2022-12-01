# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
# Сделал 4 (конкатенация, f_string, %форматирование, format)
name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
city = input("Введите ваш город: ")
concat_answer = name + ' ' + age + ' ' + city
print("Приветствую," + ' ' + concat_answer)


f_string_answer = f"Приветствую, {name} {age} {city}"
print(f_string_answer)


int_age = int(age)
percent_formatting_answer = "Приветствую, %s %d %s" % (name, int_age, city)
print(percent_formatting_answer)

format_formatting_answer = "Приветствую, {} {} {}".format(name, age, city)
print(format_formatting_answer)


