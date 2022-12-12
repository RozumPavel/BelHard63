# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно
def delete_digits(text):
    for i in text:
        if not isinstance(i, str):
            text.remove(i)

text = [1.22, "hellow", 123123, "cars", 2.32, "kick"]
delete_digits(text)
print(text)
