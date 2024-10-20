from datetime import datetime
import yaml
from lunarcalendar import Converter, Lunar


def calculate_solar_dates():
    with open("config/dates.yaml", "r") as f:
        file = yaml.safe_load(f)
        birthdays = file.get("birthdays")
        for birthday in birthdays:
            lunar = Lunar(datetime.now().year, birthday.get('lunar_month'), birthday.get('lunar_date'))
            solar = Converter.Lunar2Solar(lunar)
            print(f"Birthday: {birthday['name']}, Lunar: {lunar}, Solar: {solar}")


if __name__ == "__main__":
    calculate_solar_dates()
