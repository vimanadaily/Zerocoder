def sum_range(start, end):
    return sum(range(start, end + 1))

start = int(input("Введите начальное число: "))
end = int(input("Введите конечное число: "))

print(f"Сумма чисел от {start} до {end} равна {sum_range(start, end)}")