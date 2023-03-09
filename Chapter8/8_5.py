def describe_city(city, country="Norway"):
    """Prints city and country"""
    print(f"{city.title()} is in {country.title()}")
    
describe_city(city='norway')
describe_city("Paris", "france")
describe_city(country='Germany', city='berlin')