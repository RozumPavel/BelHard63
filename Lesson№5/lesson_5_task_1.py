# Вывести первые N чисел кратные M и больше K
n = int(input("Введите сколько чисел вывести: "))
m = int(input("Введите число которому должны быть кратны выведенные числа: "))
k = int(input("Введите число больше которого должны быть выведенные числа: "))
numbers = []
while(len(numbers) < n):
    if not k % m:
        numbers.append(k)
    k+=1
print(numbers)
