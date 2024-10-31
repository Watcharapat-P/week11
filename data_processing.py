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
class Data:
    def __init__(self, data):
        self.data = data

    def filter(self, condition):
        filtered_list = []
        for item in self.data:
            if condition(item):
                filtered_list.append(item)
        return Data(filtered_list)

    def aggregate(self, aggregation_key, aggregation_function):
        temp = []
        for items in self.data:
            temp.append(float(items[aggregation_key]))
        return aggregation_function(temp)


All_d = Data(cities)
print(All_d.data)
d1 = All_d.filter(lambda x: x['country'] == 'Italy')
d2 = All_d.filter(lambda x: x['country'] == 'Sweden')
# Let's write code to
# - print the average temperature for all the cities in Italy
print(f'Average temperature in Italy : {d1.aggregate('temperature', lambda x: sum(x)/len(x)):.2f}')
# - print the average temperature for all the cities in Sweden
print(f'Average temperature in Sweden : {d2.aggregate('temperature', lambda x: sum(x)/len(x)):.2f}')
# - print the min temperature for all the cities in Italy
print(f'Minimum temperature in Italy : {d1.aggregate('temperature', lambda x: min(x)):.2f}')
# - print the max temperature for all the cities in Sweden
print(f'Max temperature in Italy : {d2.aggregate('temperature', lambda x: max(x)):.2f}')
