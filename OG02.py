import turtle


def draw_tree(branch_length, t, angle, depth):
    """
    Рекурсивно рисует фрактальное дерево.

    :param branch_length: Длина текущей ветки
    :param t: Объект черепахи
    :param angle: Угол отклонения веток
    :param depth: Глубина рекурсии (сколько уровней веток осталось)
    """
    if depth > 0:
        # Рисуем основную ветку
        t.forward(branch_length)

        # Поворачиваемся направо для первой подветки
        t.right(angle)
        draw_tree(branch_length * 0.7, t, angle, depth - 1)

        # Возвращаемся в исходное положение и поворачиваемся налево для второй подветки
        t.left(2 * angle)
        draw_tree(branch_length * 0.7, t, angle, depth - 1)

        # Возвращаемся в начальную точку
        t.right(angle)
        t.backward(branch_length)


def main():
    # Настройка экрана
    screen = turtle.Screen()
    screen.bgcolor("black")

    # Создание черепахи
    tree_turtle = turtle.Turtle()
    tree_turtle.color("green")
    tree_turtle.speed(0)  # Максимальная скорость
    tree_turtle.width(2)  # Толщина линии

    # Начальная позиция
    tree_turtle.left(90)  # Поворачиваем черепаху вверх
    tree_turtle.penup()
    tree_turtle.setpos(0, -300)  # Начинаем снизу
    tree_turtle.pendown()

    # Рисуем дерево
    draw_tree(120, tree_turtle, 30, 8)

    # Завершение
    tree_turtle.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()