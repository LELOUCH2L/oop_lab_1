import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# # Print first 5 cities only
# for city in cities[:5]:
#     print(city)

# # Print the average temperature of all the cities
# print("The average temperature of all the cities:")
# temps = []
# for city in cities:
#     temps.append(float(city['temperature']))
# print(sum(temps)/len(temps))
# print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("All cities in Germany:")
temps = [city for city in cities if city['country'] == "Germany"]
for city in temps:
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")
temps = [city for city in cities if city['country'] == "Spain" and float(city['temperature']) > 12]
for city in temps:
    print(city)
print()

# Count the number of unique countries
print("The number of unique countries:")
temps = []
for city in cities:
    if city['country'] not in temps:
        temps.append(city['country'])
print(len(temps))
print()

# Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany:")
temps = [city for city in cities if city['country'] == "Germany"]
temperatures = [float(city['temperature']) for city in temps]
print(sum(temperatures) / len(temperatures))
print()

# Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy:")
temps = [city for city in cities if city['country'] == "Italy"]
temperatures = [float(city['temperature']) for city in temps]
print(max(temperatures))
print()
