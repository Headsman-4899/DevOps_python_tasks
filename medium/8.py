def get_season(month, day):
    if month == 3 or month == 4 or month == 5:
        return "Весна"
    elif month == 6 or month == 7 or month == 8:
        return "Лето"
    elif month == 9 or month == 10 or month == 11 or month == 12:
        return "Осень"
    else:
        return "Зима"

month = int(input("Введите месяц (число от 1 до 12): "))
day = int(input("Введите день (число от 1 до 31): "))

if (1 <= month <= 12) and (1 <= day <= 31):
    season = get_season(month, day)
    print(f"Дата {day}.{month} попадает в сезон: {season}")
else:
    print("Некорректная дата")
