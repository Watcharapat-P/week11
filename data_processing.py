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


class TableDB:
    def __init__(self):
        self.table_database = []

    def insert(self, table):
        self.table_database.append(table)

    def search(self, table_name):
        for table in self.table_database:
            if table == table_name:
                return table


class Table:
    def __init__(self, table_name='', table=None):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        filtered_list = []
        for item in self.table:
            if condition(item):
                filtered_list.append(item)
        return Table(table=filtered_list)

    def aggregate(self, aggregation_key, aggregation_function):
        temp = []
        for items in self.table:
            temp.append(float(items[aggregation_key]))
        return aggregation_function(temp)

    def __str__(self):
        return f'Table: {self.table_name}\n{self.table}'


TDB1 = TableDB()
TDB1.insert(table=cities)
TDB1.insert(table=countries)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
All_city = Table('All_city', TDB1.search(cities))
print(f'{All_city.aggregate('temperature', lambda x: sum(x)/len(x)):.2f}')

# Print all cities in Italy
Italy_cities = All_city.filter(lambda x: x['country'] == 'Italy')
print('All of the cities in Italy:')
for city in Italy_cities.table:
    print(f'{city['city']}',end=', ')
print('')
# Print the average temperature for all the cities in Italy
# Write code for me

print('The average temperature of all the cities in Italy:')
print(f'{Italy_cities.aggregate('temperature', lambda x: sum(x)/len(x)):.2f}')

# Print the max temperature for all the cities in Italy
# Write code for me
print(f'Max temperature in Italy : {Italy_cities.aggregate('temperature', lambda x: max(x)):.2f}')


# Let's write a function to filter out only items that meet the condition
Italy_cities = All_city.filter(lambda x: x['country'] == 'Italy')
Sweden_cities = All_city.filter(lambda x: x['country'] == 'Sweden')
# Let's write code to
# - print the average temperature for all the cities in Italy
print(f'Average temperature in Italy : {Italy_cities.aggregate('temperature', lambda x: sum(x)/len(x)):.2f}')
# - print the average temperature for all the cities in Sweden
print(f'Average temperature in Sweden : {Sweden_cities.aggregate('temperature', lambda x: sum(x)/len(x)):.2f}')
# - print the min temperature for all the cities in Italy
print(f'Minimum temperature in Italy : {Italy_cities.aggregate('temperature', lambda x: min(x)):.2f}')
# - print the max temperature for all the cities in Sweden
print(f'Max temperature in Italy : {Italy_cities.aggregate('temperature', lambda x: max(x)):.2f}')
