# Вывести первые N чисел кратные M и больше K
# Сделал значения всех чисел с клавиатуры
numbers_list_start = int(input("Введите с какого числа делать рассчет: "))
numbers_list_finish = int(input("Введите по какое число делать рассчет: "))
multiply_number = int(input("Введите какому числу должны быть кратны числа в ответе: "))
max_number = int(input("Введите больше какого числа должны быть числа в ответе: "))
amount_numbers = int(input("Введите сколько чисел должно быть в ответе: "))
numbers = [i for i in range(numbers_list_start, numbers_list_finish + 1) if not i % multiply_number and i > max_number]
print(numbers[:amount_numbers])
