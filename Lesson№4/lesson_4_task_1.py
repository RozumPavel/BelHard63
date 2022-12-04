# Заполнить список степенями числа 2 (от 2^1 до 2^n).
number_from_user = int(input("Введите степень до которой необходимо сделать рассчет: "))
answer = [2**i for i in range(1, number_from_user + 1)]
print(answer)
