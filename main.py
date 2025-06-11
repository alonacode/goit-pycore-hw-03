import re
from datetime import datetime, timedelta
import random


# Task 1
def get_days_from_today(date: str) -> int:
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = today - input_date
        return delta.days
    except ValueError:
        raise ValueError("Wrong format. Please use such format 'РРРР-ММ-ДД'")


print(get_days_from_today("2025-10-09"))


# Task 2
def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if min < 1 or max > 1000 or quantity > (max - min + 1) or quantity < 1:
        return []

    numbers = set()

    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(numbers)

print(get_numbers_ticket(1, 10, 6))


# Task 3
def normalize_phone(phone_number: str) -> str:
    phone_number = phone_number.strip()

    if phone_number.startswith('+'):
        return '+' + re.sub(r'\D', '', phone_number[1:])
    cleaned = re.sub(r'\D', '', phone_number)

    if cleaned.startswith('380'):
        return '+' + cleaned
    return '+38' + cleaned


def normalize_phone_list(numbers: list[str]) -> list[str]:
    return [normalize_phone(number) for number in numbers]

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

normalized = normalize_phone_list(raw_numbers)
print(normalized)


# Task 4
def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    upcoming_birthdays: list[dict[str, str]] = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= end_date:
            congrats_date = birthday_this_year

            if congrats_date.weekday() == 5:  # Субота
                congrats_date += timedelta(days=2)
            elif congrats_date.weekday() == 6:  # Неділя
                congrats_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congrats_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.06.15"},
    {"name": "Jane Smith", "birthday": "1990.07.15"}
]
print(get_upcoming_birthdays(users))






