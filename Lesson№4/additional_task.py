# Сгенерировать два списка рандомных чисел и посчитать количество общих элементов
import random
from random import randint
random_numbers_first = [randint(0,50) for i in range(10)]
random_numbers_second = [randint(-10,40) for i in range(10)]

first_set = set(random_numbers_first)
second_set = set(random_numbers_second)

first_set_second_set = first_set & second_set
answer = len(first_set_second_set)
print(answer)
