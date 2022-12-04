word_from_user = input("Введите ваш текст: ")
answer = {symbol: word_from_user.count(symbol) for symbol in word_from_user}
print(answer)