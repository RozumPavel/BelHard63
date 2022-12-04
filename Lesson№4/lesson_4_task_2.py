word_from_user = input("Введите ваш текст: ")
answer = {i: word_from_user.count(i) for i in word_from_user}
print(answer)
