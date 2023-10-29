import csv
from datetime import datetime as dt
import json


def get_most_crime_for_year(year, filename):
	with open(filename) as f:
		reader = csv.reader(f)
		columns = reader.__next__()
		primary_type_column_index = columns.index('Primary Type')
		date_column_index = columns.index('Date')
		date_format = '%m/%d/%Y %I:%M:%S %p'
		crimes_count = dict()
		for row in reader:
			if dt.strptime(row[date_column_index], date_format).year != year:
				continue
			if row[5] in crimes_count.keys():
				crimes_count[row[primary_type_column_index]] += 1
			else:
				crimes_count[row[primary_type_column_index]] = 1
		sorted_crimes = sorted(crimes_count.items(), key=lambda item: item[1], reverse=True)
		print(sorted_crimes[0][0])
		
get_most_crime_for_year(2015, 'Crimes.csv')

# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию
def get_ancestors_count(row, class_list, current_count, class_cache):
	child_list = [cl for cl in class_list if (row['name'] in cl['parents']) and (cl['name'] not in class_cache)]
	class_cache.extend([x['name'] for x in child_list if x['name'] not in class_cache])
	current_count += len(child_list)
	for child in child_list:
		current_count = get_ancestors_count(child, class_list, current_count, class_cache)
	return current_count

def get_classes_count():
	input_json = input()
	class_list = json.loads(input_json)
	result = dict()
	for row in class_list:
		result[row['name']] = get_ancestors_count(row, class_list, 1, list())
	sorted_dict = sorted(result.items(), key=lambda x: x[0])
	for row in sorted_dict:
		print(f"{row[0]} : {row[1]}")

input_json = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'
get_classes_count()