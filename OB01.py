class Task:
    """
    Класс Task описывает одну задачу с полями:
      - description: текстовое описание задачи
      - deadline: строка со сроком выполнения (можно в любом читаемом формате)
      - is_done: флаг, выполнена ли задача (True/False)
    """
    def __init__(self, description: str, deadline: str):
        self.description = description
        self.deadline = deadline
        self.is_done = False  # по умолчанию задача не выполнена

    def mark_done(self):
        """Отметить задачу как выполненную."""
        self.is_done = True

    def __str__(self):
        """Красивый вывод задачи: статус, описание и строка-срок."""
        status = "✓" if self.is_done else "✗"
        return f"[{status}] {self.description} (срок: {self.deadline})"


class TaskManager:
    """
    Класс TaskManager хранит список задач и умеет:
      - добавлять новую задачу
      - отмечать задачу выполненной по её индексу
      - выводить список всех текущих (не выполненных) задач
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, description: str, deadline: str):
        """
        Добавить новую задачу.
        deadline — любая строка, описывающая срок.
        """
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Задача добавлена: {task}")

    def mark_task_done(self, index: int):
        """
        Отметить задачу выполненной по её индексу (начиная с 1).
        """
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].mark_done()
            print(f"Задача #{index} отмечена как выполненная.")
        else:
            print("Неверный индекс задачи.")

    def show_pending_tasks(self):
        """
        Вывести все задачи, у которых is_done == False.
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
    Основная программа: меню добавления, отметки и просмотра задач.
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
            dl = input("Срок выполнения (любой формат): ").strip()
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
