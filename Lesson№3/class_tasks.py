request = input("Введите трехзначное число: ")
x = int(request[0])
y = int(request[1])
z = int(request[2])
print(x)
print(y)
print(z)
total = sum([x, y, z])
print(total)

request_to_user = input("Введите предложение, состоящее из трех слов: ")
first_word = request_to_user[:request_to_user.find(' ')]
last_word = request_to_user[request_to_user.rfind(' ') + 1:]
center_word = request_to_user[request_to_user.find(' '): request_to_user.rfind(' ') + 1]
answer = last_word + center_word + first_word
print(answer)

