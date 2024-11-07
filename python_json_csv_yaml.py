import json  # is built in library no need to install
import yaml  # is external library you need to install with 'pip install pyyaml'
import csv

"""
r = read
w = write

"""

json_data_to_write = [

    {'Name': 'John', 'Age': 30, 'City': 'New York'},
    {'Name': 'Adam', 'Age': 29, 'City': 'Berlin'},
    {'Name': 'Manual', 'Age': 35, 'City': 'Munich'}
]

"""
w checks if there is a file already if there is none, it creates one

"""

with open('data.json', 'w') as data_json_file:
    json.dump(json_data_to_write, data_json_file)

print('-----------------------------------------------------')

with open('data.json', 'r') as data_json_file:
    data = json.load(data_json_file)
    print(data)
    print(type(data))

json_data_to_write = [

    {'Name': 'John', 'Age': 30, 'City': 'New York'},
    {'Name': 'Adam', 'Age': 29, 'City': 'Berlin'},
    {'Name': 'Manual', 'Age': 35, 'City': 'Munich'},
    {'Name': 'Josef', 'Age': 40, 'City': 'Zürich'}
]


with open('new_data.json', 'w') as new_data_json_file:
    json.dump(json_data_to_write, new_data_json_file)


print('--------------------------------------------------------')


with open("new_data.json", 'r') as new_data_json_file:
    data = json.load(new_data_json_file)
    print(data)
    print(type(data))


yaml_data_to_write = [

     {'Name': 'John', 'Age': 30, 'City': 'New York'},
    {'Name': 'Adam', 'Age': 29, 'City': 'Berlin'},
    {'Name': 'Manual', 'Age': 35, 'City': 'Munich'},
    {'Name': 'Josef', 'Age': 40, 'City': 'Zürich'}
]

with open('data.yml','w') as data_yaml_file:
    yaml.dump(yaml_data_to_write, data_yaml_file)

with open('data.yml', 'r') as data_yaml_file:
    data = yaml.safe_load(data_yaml_file)
    print(data)
    print(type(data))

print("--------------------------------------")


yaml_data_to_write = [

     {'Name': 'John', 'Age': 30, 'City': 'New York'},
    {'Name': 'Adam', 'Age': 29, 'City': 'Berlin'},
    {'Name': 'Manual', 'Age': 35, 'City': 'Munich'},
    {'Name': 'Josef', 'Age': 40, 'City': 'Zürich'}
]


with open('new_data.yml', 'w') as new_data_yaml_file:
    yaml.dump(yaml_data_to_write, new_data_yaml_file)

with open('new_data.yml', 'r') as new_data_yaml_file:
    data = yaml.safe_load(new_data_yaml_file)
    print(data)
    print(type(data))

with open('data.csv', 'r') as data_csv_file:
    print(data_csv_file.read())
    csv_reader = csv.reader(data_csv_file)
    print(list(csv_reader))
    for row in csv_reader:
        print(row)

csv_data_to_write = [
    ['Name': 'John', 'Age': 30, 'City': 'New York'],
    ['Name': 'Adam', 'Age': 29, 'City': 'Berlin'],
    ['Name': 'Manual', 'Age': 35, 'City': 'Munich'],
    ['Name': 'Josef', 'Age': 40, 'City': 'Zürich']
]

with open('new_data.csv', 'w') as new_data_csv_file:
    csv_writer = csv.writer(new_data_csv_file)
    csv_writer.writerows(csv_data_to_write)

print('--------------------------------------------------')


