# Вывести четные числа от 2 до N по 5 в строку
n = int(input("Введите до какого числа вывести четные числа: "))
numbers = [2*i for i in range(1, n // 2 + 1)]
for i in range(0, len(numbers), 5):
    print(numbers[i:i + 5], sep='')