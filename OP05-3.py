# На основе OP04-1 добавил обработку исключений

def sum_range(start, end):
    return sum(range(start, end + 1))

while True:
    try:
        start = int(input("Введите начальное число: "))
        end = int(input("Введите конечное число: "))

        # Проверка: start не должен быть больше end
        if start > end:
            print("Ошибка: Начальное число не может быть больше конечного. Попробуйте снова.")
            continue

        # Если всё корректно, выходим из цикла
        break
    except ValueError:
        print("Ошибка: Введите корректные целые числа.")

# Вывод результата
print(f"Сумма чисел от {start} до {end} равна {sum_range(start, end)}")
