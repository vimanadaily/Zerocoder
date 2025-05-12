import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return f"{self.name} издаёт звук."

class Bird(Animal):
    def make_sound(self):
        return f"{self.name} чирикает."

class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} рычит."

class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} шипит."

class ZooKeeper:
    def __init__(self, name):
        self.name = name

class Veterinarian:
    def __init__(self, name):
        self.name = name

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def save_to_file(self, filename="zoo_data.pkl"):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_from_file(filename="zoo_data.pkl"):
        with open(filename, 'rb') as f:
            return pickle.load(f)

def main():
    zoo = Zoo()

    while True:
        print("\nУправление зоопарком:")
        print("1. Добавить животное")
        print("2. Добавить сотрудника")
        print("3. Показать всех животных")
        print("4. Показать всех сотрудников")
        print("5. Издать звуки животных")
        print("6. Сохранить зоопарк")
        print("7. Загрузить зоопарк")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Имя животного: ")
            age = input("Возраст животного: ")
            print("Тип животного: 1 - Птица, 2 - Млекопитающее, 3 - Рептилия")
            atype = input("Ваш выбор: ")
            try:
                age = int(age)
                if atype == '1':
                    animal = Bird(name, age)
                elif atype == '2':
                    animal = Mammal(name, age)
                elif atype == '3':
                    animal = Reptile(name, age)
                else:
                    print("Неверный выбор типа животного.")
                    continue
                zoo.add_animal(animal)
                print(f"Животное {name} добавлено.")
            except ValueError:
                print("Ошибка: возраст должен быть числом.")

        elif choice == '2':
            name = input("Имя сотрудника: ")
            print("Тип сотрудника: 1 - Смотритель, 2 - Ветеринар")
            stype = input("Ваш выбор: ")
            if stype == '1':
                staff = ZooKeeper(name)
            elif stype == '2':
                staff = Veterinarian(name)
            else:
                print("Неверный выбор типа сотрудника.")
                continue
            zoo.add_staff(staff)
            print(f"Сотрудник {name} добавлен.")

        elif choice == '3':
            if not zoo.animals:
                print("Животные отсутствуют.")
            else:
                for a in zoo.animals:
                    print(f"{a.name} ({type(a).__name__}), возраст: {a.age}")

        elif choice == '4':
            if not zoo.staff:
                print("Сотрудники отсутствуют.")
            else:
                for s in zoo.staff:
                    print(f"{s.name} ({type(s).__name__})")

        elif choice == '5':
            if not zoo.animals:
                print("Нет животных для звуков.")
            else:
                for animal in zoo.animals:
                    print(animal.make_sound())

        elif choice == '6':
            zoo.save_to_file()
            print("Зоопарк сохранён.")

        elif choice == '7':
            zoo = Zoo.load_from_file()
            print("Зоопарк загружен.")

        elif choice == '0':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()

