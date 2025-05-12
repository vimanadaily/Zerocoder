from abc import ABC, abstractmethod


# Шаг 1: Абстрактный класс оружия
class Weapon(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        """Название оружия (для вывода в консоль)."""
        pass

    @abstractmethod
    def attack(self) -> str:
        """
        Описание атаки: возвращает строку,
        например "удар мечом" или "выстрел из лука".
        """
        pass


# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    @property
    def name(self) -> str:
        return "меч"

    def attack(self) -> str:
        # Здесь возвращаем, как звучит атака мечом
        return "удар мечом"


class Bow(Weapon):
    @property
    def name(self) -> str:
        return "лук"

    def attack(self) -> str:
        # Здесь возвращаем, как звучит атака из лука
        return "удар из лука"


# Шаг 3: Класс Fighter, открытый для расширения оружием, но закрытый для правки механизма боя
class Fighter:


    def __init__(self, name: str):
        self.name = name
        self.weapon: Weapon = None  # пока нет оружия

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.name}.")

    def attack(self, monster: "Monster"):
        if not self.weapon:
            print(f"{self.name} пытается атаковать, но у него нет оружия!")
            return

        # Получаем описание атаки из объекта оружия
        action_desc = self.weapon.attack()
        # Выводим, что именно делает боец
        print(f"{self.name} наносит {action_desc}.")
        # Упрощённая логика: после одного удара монстр побеждён
        print(f"{monster.name} побежден!")


# Класс Monster — просто держит имя монстра
class Monster:
    def __init__(self, name: str):
        self.name = name


# Шаг 4: Демонстрация работы без правки существующих классов
def main():
    # Создаём бойца и монстра
    hero = Fighter("Боец")
    beast = Monster("Монстр")

    # Бой с мечом
    hero.change_weapon(Sword())
    hero.attack(beast)

    print()  # пустая строка для читабельности

    # Бой с луком
    hero.change_weapon(Bow())
    hero.attack(beast)



if __name__ == "__main__":
    main()
