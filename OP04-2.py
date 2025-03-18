import math

def square(side):
    perimeter = 4 * side  # Периметр = 4 * сторона
    area = side ** 2  # Площадь = сторона^2
    diagonal = side * math.sqrt(2)  # Диагональ = сторона * sqrt(2)
    return perimeter, area, diagonal  # Возвращаем кортеж из 3 значений

side = float(input("Введите длину стороны квадрата: "))

perimeter, area, diagonal = square(side)

# Вывод результатов
print(f"Периметр: {perimeter}")
print(f"Площадь: {area}")
print(f"Диагональ: {diagonal}")
