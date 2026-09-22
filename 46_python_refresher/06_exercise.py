def get_adult(ages):
    result = []
    for age in ages:
        if age >= 18:
            result.append(age)
    return result

print(get_adult([12, 18, 25, 15, 31, 17]))