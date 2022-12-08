# Вывести первые N чисел кратные M и больше K
n = int(input("Введите сколько чисел вывести: "))
m = int(input("Введите число которому должно быть кратно введенное вами: "))
k = int(input("Введите число больше которого должны быть выведенные числа: "))
numbers = []
while (len(numbers)<n):
    number_from_user = input("Введите ваше число: ")
    if not number_from_user.isdigit():
        number_from_user = input("Вы ввели не число.Введите число: ")
    if not int(number_from_user) % m and int(number_from_user) > k:
        numbers.append(number_from_user)
    print(numbers)      
