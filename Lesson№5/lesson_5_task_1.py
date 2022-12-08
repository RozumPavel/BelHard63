# Вывести первые N чисел кратные M и больше K
numbers = []
while (len(numbers)<5):
    number_from_user = input("Введите число: ")
    while not number_from_user.isdigit():
        number_from_user = input("Введите ваше число: ")
    if not int(number_from_user) % 7 and int(number_from_user) > 10:
        numbers.append(number_from_user)
    print(numbers)
      
