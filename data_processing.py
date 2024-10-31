import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print all cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(city['city'])
print("All the cities in", my_country, ":")
print(temps)
print()

# Print the average temperature for all the cities in Italy
# Write code for me
temp = []
for city in cities:
    if city['country'] == my_country:
        temp.append(float(city['temperature']))
print(temp)
print(f'Average temperature : {sum(temp)/len(temp):.2f}')

# Print the max temperature for all the cities in Italy
# Write code for me
print(f'Max temperature : {max(temp):.2f}')


# Let's write a function to filter out only items that meet the condition
def filter(condition, dict_list):
    filtered_list = []
    for item in dict_list:
        if condition(item):
            filtered_list.append(item)
    return filtered_list


x = filter(lambda x: float(x['latitude']) >= 60.0, cities)
for item in x:
    print(item)


# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    temp = []
    for items in dict_list:
        temp.append(float(items[aggregation_key]))
    return aggregation_function(temp)


# Let's write code to
# - print the average temperature for all the cities in Italy
print(f'Average temperature in Italy : {aggregate('temperature', lambda x: sum(x)/len(x), filter(lambda x: x['country'] == 'Italy', cities)):.2f}')
# - print the average temperature for all the cities in Sweden
print(f'Average temperature in Sweden : {aggregate('temperature', lambda x: sum(x)/len(x), filter(lambda x: x['country'] == 'Sweden', cities)):.2f}')
# - print the min temperature for all the cities in Italy
print(f'Minimum temperature in Italy : {aggregate('temperature', lambda x: min(x), filter(lambda x: x['country'] == 'Italy', cities)):.2f}')
# - print the max temperature for all the cities in Sweden
print(f'Max temperature in Italy : {aggregate('temperature', lambda x: max(x), filter(lambda x: x['country'] == 'Sweden', cities)):.2f}')
