# Запрос ввода от пользователя
user_text = input("Введите текст для добавления в файл: ")

# Открываем файл в режиме добавления ('a') и записываем текст
with open("user_data.txt", "a", encoding="utf-8") as file:
    file.write(user_text + "\n")  # Добавляем текст и перевод строки

print("Текст успешно добавлен в файл user_data.txt")

# Читаем и выводим всё содержимое файла
with open("user_data.txt", "r", encoding="utf-8") as file:
    print("Содержимое файла:")
    print(file.read())  # Читаем и выводим весь текст файла