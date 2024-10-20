from datetime import datetime
import yaml
from lunarcalendar import Converter, Lunar

this_year = datetime.now().year


def add_calendar_event(name, lunar_birthday):
    for i in range(10):
        lunar = Lunar(
            this_year + i, lunar_birthday["lunar_month"], lunar_birthday["lunar_date"]
        )
        solar = Converter.Lunar2Solar(lunar)
        print(f"{name}: {solar}")


def mark_future_birthdays():
    with open("config/dates.yaml", "r") as f:
        file = yaml.safe_load(f)
        birthdays = file.get("birthdays")
        for birthday in birthdays:
            add_calendar_event(birthday["name"], birthday)


if __name__ == "__main__":
    mark_future_birthdays()
