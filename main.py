print("Генератор мемов запущен!")
text_type = input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: ")
top_text = ""
bottom_text = ""
if text_type == "1":
    bottom_text = input("Введите нижний текст: ")
if text_type == "2":
    top_text = input("Введите верхний текст: ")
    bottom_text = input("Введите нижний текст: ")
print(top_text, bottom_text)


