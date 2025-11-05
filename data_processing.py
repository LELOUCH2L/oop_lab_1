import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))


# A function to filter out only items that meet the condition
def filter(condition, dict_list):
    temps = [item for item in dict_list if condition(item)]
    return temps


# A function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    temps = [item[aggregation_key] for item in dict_list]
    return aggregation_function(temps)


# Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(aggregate('temperature', lambda x: sum(map(float, x)) / len(x), cities))
print()

# Print all cities in Germany
print("All cities in Germany:")
temps = filter(lambda x: x['country'] == 'Germany', cities)
for city in temps:
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")
temps = filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12, cities)
for city in temps:
    print(city)
print()

# Count the number of unique countries
print("The number of unique countries:")
print(aggregate('country', lambda x: len(set(x)), cities))
print()

# Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany:")
temps = filter(lambda x: x['country'] == 'Germany', cities)
print(aggregate('temperature', lambda x: sum(map(float, x)) / len(x), temps))
print()

# Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy:")
temps = filter(lambda x: x['country'] == 'Italy', cities)
print(aggregate('temperature', lambda x: max(map(float, x)), temps))
print()
