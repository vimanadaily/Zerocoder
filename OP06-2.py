import arithmetic

# Тестирование функций
a, b = 15, 3

print(f"{a} + {b} = {arithmetic.plus(a, b)}")
print(f"{a} - {b} = {arithmetic.minus(a, b)}")
print(f"{a} * {b} = {arithmetic.multiply(a, b)}")
print(f"{a} / {b} = {arithmetic.division(a, b)}")

# Проверка деления на 0
print(f"{a} / 0 = {arithmetic.division(a, 0)}")
