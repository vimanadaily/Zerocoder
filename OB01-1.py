# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.

class Store:
    """
    Класс Store описывает магазин с названием, адресом и ассортиментом товаров.
    """

    def __init__(self, name: str, address: str):
        """
        Конструктор:
          - name    : название магазина (строка)
          - address : адрес магазина (строка)
          - items   : словарь {название товара: цена}, изначально пустой
        """
        self.name = name
        self.address = address
        self.items = {}  # здесь будем хранить товары и их цены

    def add_item(self, item_name: str, price: float):
        """
        Добавление товара в ассортимент.
        Если товар уже есть – его цена перезапишется.
        """
        self.items[item_name] = price
        print(f"✅ Товар '{item_name}' добавлен/обновлён с ценой {price} ₽.")

    def remove_item(self, item_name: str):
        """
        Удаление товара из ассортимента.
        Если товара нет – сообщаем об этом.
        """
        if item_name in self.items:
            del self.items[item_name]
            print(f"🗑 Товар '{item_name}' удалён из ассортимента.")
        else:
            print(f"⚠ Товар '{item_name}' не найден. Нечего удалять.")

    def get_price(self, item_name: str):
        """
        Возвращает цену товара по его названию.
        Если товара нет – возвращает None.
        """
        return self.items.get(item_name)

    def update_price(self, item_name: str, new_price: float):
        """
        Обновление цены существующего товара.
        Если товара нет – выводим предупреждение.
        """
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"✏ Цена товара '{item_name}' обновлена на {new_price} ₽.")
        else:
            print(f"⚠ Товар '{item_name}' не найден. Нельзя обновить цену.")


# Если вы сохраняете этот файл как store.py, ниже код можно поместить в main.py
if __name__ == "__main__":
    # Шаг 2: создаём несколько магазинов
    store1 = Store("Гипермаркет Магия",    "ул. Ленина, 10")
    store2 = Store("Минимаркет У дома",   "пр. Мира, 25")
    store3 = Store("Экопродукты",          "ул. Зелёная, 5")

    # Добавляем товары в каждый магазин
    store1.add_item("apples",  0.5)
    store1.add_item("bananas", 0.75)
    store1.add_item("milk",    1.2)

    store2.add_item("bread",   1.0)
    store2.add_item("eggs",    2.5)
    store2.add_item("water",   0.8)

    store3.add_item("organic apples",  1.5)
    store3.add_item("organic bananas", 1.8)
    store3.add_item("organic milk",    2.3)

    # Шаг 3: тестируем методы на одном магазине (store1)
    print("\n=== Тестирование магазина:", store1.name, "===\n")

    # Получаем цену существующего товара
    price = store1.get_price("apples")
    print(f"Цена 'apples': {price} ₽")  # ожидаем 0.5

    # Пытаемся получить цену несуществующего товара
    missing = store1.get_price("chocolate")
    print(f"Цена 'chocolate': {missing}")  # ожидаем None

    # Обновляем цену существующего товара
    store1.update_price("bananas", 0.85)

    # Пытаемся обновить цену несуществующего товара
    store1.update_price("chocolate", 1.5)

    # Удаляем существующий товар
    store1.remove_item("milk")

    # Пытаемся удалить снова тот же товар
    store1.remove_item("milk")

    # Выводим текущее состояние ассортимента store1
    print(f"\nТекущий ассортимент '{store1.name}':")
    for item, price in store1.items.items():
        print(f" - {item}: {price} ₽")
