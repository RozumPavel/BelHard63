
def delete_digits(text):
    for i in text:
        if not isinstance(i, str):
            text.remove(i)

text = [123, "hellow", 123123, "cars"]
delete_digits(text)
print(text)