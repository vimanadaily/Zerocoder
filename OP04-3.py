def bank(a, years):
    for _ in range(years):
        a = a + (a * 10 / 100)
    return a

a = float(input("Введите сумму вклада: "))
years = int(input("Введите срок вклада (в годах): "))

final_amount = bank(a, years)

print(f"Через {years} лет на счету будет: {final_amount}")
