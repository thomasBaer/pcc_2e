
import sys

sys.clear()

def city_country(city, country):
    """Return a full formated city country sentence"""
    country = country.title()
    city = city.title()
    value = f"The captial of {country} is {city}."
    return value

print(city_country("berlin", "deutschland"))
print(city_country("vienna", "AUSTRIA"))
print(city_country("london", "Great Britain"))

