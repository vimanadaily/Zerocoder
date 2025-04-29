class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, new_name):
        self.__name = new_name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'

    def add_user(self, user_list, new_user):
        if isinstance(new_user, User):
            user_list.append(new_user)
            print(f"Пользователь {new_user.get_name()} добавлен.")
        else:
            print("Ошибка: можно добавлять только объекты класса User.")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь с ID {user_id} удалён.")
                return
        print(f"Пользователь с ID {user_id} не найден.")


# Пример использования
users = []
admin = Admin(1, "Иван")
user1 = User(2, "Ольга")
user2 = User(3, "Максим")

admin.add_user(users, user1)
admin.add_user(users, user2)
admin.remove_user(users, 2)

# Проверка оставшихся пользователей
for u in users:
    print(f"ID: {u.get_id()}, Имя: {u.get_name()}, Уровень доступа: {u.get_access_level()}")