#Напишите программу на Python с использованием модуля tkinter, которая позволяет пользователю ввести свое имя в окно
# ввода, а затем выводит на экран сообщение "Привет, [имя]!".

import tkinter as tk

def greet():
    name = entry.get()
    label.config(text=f"Привет, {name}!")

# Создание окна
root = tk.Tk()
root.title("Приветствие")

# Метка для вывода результата
label = tk.Label(root, text="Введите свое имя")
label.pack()

# Поле ввода
entry = tk.Entry(root)
entry.pack()

# Кнопка
button = tk.Button(root, text="Поздороваться", command=greet)
button.pack()


# Запуск главного цикла
root.mainloop()