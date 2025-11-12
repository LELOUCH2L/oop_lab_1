import csv, os
from pathlib import Path


class DataLoader:
    def __init__(self, base_path=None):
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)
    
    def load_csv(self, filename):
        filepath = self.base_path / filename
        data = []
        
        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))
        
        return data


class DB:
    def __init__(self):
        self.tables = []

    def insert(self, table):
        self.tables.append(table)

    def search(self, table_name):
        for table in self.tables:
            if table.table_name == table_name:
                return table


class Table:
    def __init__(self, name, dict_list):
        self.table_name = name
        self.table = dict_list

    def filter(self, condition):
        temps = [item for item in self.table if condition(item)]
        return Table(f'{self.table_name}_filtered', temps)

    def aggregate(self, aggregation_function, aggregation_key):
        try:
            temps = [float(item[aggregation_key]) for item in self.table]
        except ValueError:
            temps = [(item[aggregation_key]) for item in self.table]
        return aggregation_function(temps)
    
    def join(self, another_table, common_key):
        joined_table = []
        for data1 in self.table:
            for data2 in another_table.table:
                if data1[common_key] == data2[common_key]:
                    data1.update(data2)
                    break
            joined_table.append(data1)
        return Table('joined table', joined_table)


    def __str__(self):
        return self.table_name + ':' + str(self.table)


loader = DataLoader()
cities = loader.load_csv('Cities.csv')
table1 = Table('cities', cities)
countries = loader.load_csv('Countries.csv')
table2 = Table('countries', countries)

my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)

my_table1 = my_DB.search('cities')
print("List all cities in Italy:") 
my_table1_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
print(my_table1_filtered)
print()

print("Average temperature for all cities in Italy:")
print(my_table1_filtered.aggregate(lambda x: sum(x)/len(x), 'temperature'))
print()

my_table2 = my_DB.search('countries')
print("List all non-EU countries:") 
my_table2_filtered = my_table2.filter(lambda x: x['EU'] == 'no')
print(my_table2_filtered)
print()

print("Number of countries that have coastline:")
print(my_table2.filter(lambda x: x['coastline'] == 'yes').aggregate(lambda x: len(x), 'coastline'))
print()

my_table3 = my_table1.join(my_table2, 'country')
print("First 5 entries of the joined table (cities and countries):")
for item in my_table3.table[:5]:
    print(item)
print()

print("Cities whose temperatures are below 5.0 in non-EU countries:")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'no').filter(lambda x: float(x['temperature']) < 5.0)
print(my_table3_filtered.table)
print()

print("The min and max temperatures for cities in EU countries that do not have coastlines")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'yes').filter(lambda x: x['coastline'] == 'no')
print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), 'temperature'))
print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), 'temperature'))
print()