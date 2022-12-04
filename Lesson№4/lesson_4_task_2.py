# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

# 1
word_from_user = input("Введите ваш текст: ")
answer = {i: word_from_user.count(i) for i in word_from_user}
print(answer)

# 2
answer = {}
for i in word_from_user:
    answer[i] = word_from_user.count(i)
print(answer)
