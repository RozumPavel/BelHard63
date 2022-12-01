# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
# Сделал 4 (конкатенация, f_string, %форматирование, format)
name = input("Введите ваше имя: ")
age =  input("Введите ваш возраст: ")
city = input("Введите ваш город: ")
answer = name + ' ' + age + ' ' + city
print("Приветствую," + ' ' + answer)

answer1 = f"Приветствую, {name} {age} {city}"
print(answer1)

int_age = int(age)
answer2 = "Приветствую, %s %d %s" % (name, int_age, city)
print(answer2)
