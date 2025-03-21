def plus(a, b):
    """Функция сложения"""
    return a + b

def minus(a, b):
    """Функция вычитания"""
    return a - b

def multiply(a, b):
    """Функция умножения"""
    return a * b

def division(a, b):
    """Функция деления (с проверкой на 0)"""
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b
