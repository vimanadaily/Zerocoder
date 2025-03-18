import random

# Варианты выбора
choices = ["камень", "ножницы", "бумага"]

# Очки игроков
player_score = 0
computer_score = 0

print("Добро пожаловать в игру 'Камень, ножницы, бумага'! Игра идет до 3 побед.")

# Цикл игры до 3 побед
while player_score < 3 and computer_score < 3:
    # Игрок делает выбор
    player_choice = input("\nВыберите (камень, ножницы, бумага): ").lower()

    # Проверяем корректность ввода
    if player_choice not in choices:
        print("Некорректный ввод! Попробуйте снова.")
        continue

    # Компьютер делает случайный выбор
    computer_choice = random.choice(choices)
    print(f"Компьютер выбрал: {computer_choice}")

    # Определяем победителя раунда
    if player_choice == computer_choice:
        print("Ничья!")
    elif (player_choice == "камень" and computer_choice == "ножницы") or \
         (player_choice == "ножницы" and computer_choice == "бумага") or \
         (player_choice == "бумага" and computer_choice == "камень"):
        print("Вы выиграли этот раунд!")
        player_score += 1
    else:
        print("Компьютер выиграл этот раунд!")
        computer_score += 1

    # Выводим текущий счет
    print(f"Счет: Игрок {player_score} - {computer_score} Компьютер")

# Определяем победителя игры
if player_score == 3:
    print("\n🎉 Поздравляем! Вы выиграли игру! 🎉")
else:
    print("\n😢 Компьютер победил. Попробуйте еще раз! 😢")
