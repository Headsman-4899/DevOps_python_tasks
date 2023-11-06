def is_valid_date(date_str):
    day, month, year = map(int, date_str.split('.'))
    if 1 <= month <= 12 and 1 <= day <= 31:
        if (month in [4, 6, 9, 11] and day > 30) or (month == 2 and day > 29):
            return False
        elif month == 2 and day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            return False
        return True
    else:
        return False

date_str = "30.12.2020"
if is_valid_date(date_str):
    print(f"{date_str} - корректная дата")
else:
    print(f"{date_str} - некорректная дата")
