import random

students = [
    "Анна", "Алена", "Мария", "Петр", "Алексей", "Виктор", "Анна", "Алена", "Мария", "Петр", "Алексей", "Виктор"
]

# Удаляем повторяющиеся имена с помощью множества
unique_students = list(set(students))

# Проверяем, что в списке осталось минимум 5 уникальных имен
if len(unique_students) < 5:
    print("Ошибка: В списке должно быть минимум 5 уникальных учеников.")
else:
    # Выбираем 5 случайных имен без повторений
    selected_students = random.sample(unique_students, 5)

    # Выводим результат
    print("Ученики, которые будут отвечать на уроке:")
    for name in selected_students:
        print(name)
