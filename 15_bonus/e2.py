from os import path
import csv

with open(path.join(path.curdir, '15_bonus', 'files', 'weather.csv'), 'r') as file:
    data = list(csv.reader(file))

city = input('Provide a city name: ')

for row in data[1:]:
    if row[0] == city:
        print(row[1])
