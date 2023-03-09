def city_country(city, country):
    """Returns formatted City Country"""
    formatted_city_country = f"{city.title()}, {country.title()}"
    return formatted_city_country

location = city_country('Ontario', 'Canada')
print(location)

location = city_country('London', 'England')
print(location)

location = city_country('glascow', 'scotland')
print(location)