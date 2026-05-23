# Create a function get_phone() that takes country, area, first, last
# Call it using positional arguments in correct order
# Call it again using keyword arguments in any order
# Store one result in a variable and print it

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)

# Positional arguments - order matters
print(get_phone("England", "London", "Julie", "Williams"))

# Keyword arguments - order doesn't matter
print(get_phone(last="Williams", area="England", country="London", first="Julie"))