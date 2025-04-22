from datetime import datetime

class Task:
    """
    Класс Task описывает одну задачу с полями:
      - description: текстовое описание задачи
      - deadline: срок выполнения (объект datetime)
      - is_done: флаг, выполнена ли задача (True/False)
    """
    def __init__(self, description: str, deadline: datetime):
        # Описываем основные атрибуты задачи
        self.description = description
        self.deadline = deadline
        self.is_done = False  # по умолчанию задача не выполнена

    def mark_done(self):
        """Отметить задачу как выполненную."""
        self.is_done = True

    def __str__(self):
        """Красивый вывод задачи: описание, срок и статус."""
        status = "✓" if self.is_done else "✗"
        # форматируем дату в читаемый вид
        deadline_str = self.deadline.strftime("%Y-%m-%d %H:%M")
        return f"[{status}] {self.description} (до {deadline_str})"


class TaskManager:
    """
    Класс TaskManager хранит список задач и умеет:
      - добавлять новую задачу
      - отмечать задачу выполненной по её индексу
      - выводить список всех текущих (не выполненных) задач
    """
    def __init__(self):
        self.tasks = []  # здесь будут храниться объекты Task

    def add_task(self, description: str, deadline_str: str):
        """
        Добавить новую задачу.
        deadline_str — строка в формате 'YYYY-MM-DD HH:MM'.
        Мы её парсим в datetime.
        """
        try:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Неправильный формат даты. Используйте YYYY-MM-DD HH:MM")
            return

        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Задача добавлена: {task}")

    def mark_task_done(self, index: int):
        """
        Отметить задачу выполненной по её индексу (начиная с 1).
        Проверяем границы списка.
        """
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].mark_done()
            print(f"Задача #{index} отмечена как выполненная.")
        else:
            print("Неверный индекс задачи.")

    def show_pending_tasks(self):
        """
        Вывести все задачи, у которых is_done == False.
        Если таких нет — вывести уведомление.
        """
        pending = [t for t in self.tasks if not t.is_done]
        if not pending:
            print("Нет невыполненных задач. Отличная работа!")
        else:
            print("Невыполненные задачи:")
            for i, task in enumerate(pending, start=1):
                print(f"{i}. {task}")


def main():
    """
    Основная программа: в цикле предлагает пользователю
    добавить задачу, отметить задачу выполненной или выйти.
    """
    manager = TaskManager()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить задачу")
        print("2. Отметить задачу выполненной")
        print("3. Показать текущие задачи")
        print("4. Выход")

        choice = input("Введите номер действия (1-4): ").strip()
        if choice == "1":
            desc = input("Описание задачи: ").strip()
            dl = input("Срок (YYYY-MM-DD HH:MM): ").strip()
            manager.add_task(desc, dl)
        elif choice == "2":
            idx = input("Номер задачи для отметки: ").strip()
            if idx.isdigit():
                manager.mark_task_done(int(idx))
            else:
                print("Пожалуйста, введите число.")
        elif choice == "3":
            manager.show_pending_tasks()
        elif choice == "4":
            print("Выход из программы. До встречи!")
            break
        else:
            print("Некорректный ввод. Выберите пункт 1-4.")

if __name__ == "__main__":
    main()
