import datetime
from lunarcalendar import Converter, Solar, Lunar, DateNotExist

solar = Solar(2018, 1, 1)
print(solar)
lunar = Converter.Solar2Lunar(solar)
print(lunar)
solar = Converter.Lunar2Solar(lunar)
print(solar)
print(solar.to_date(), type(solar.to_date()))
