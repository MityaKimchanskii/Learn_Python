# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#
#     temperatures = []
#
#     for row in data:
#         if row[1] != 'temp':
#             temperature = int(row[1])
#             temperatures.append(temperature)

import  pandas

data = pandas.read_csv('weather_data.csv')
# print(data)
# print((data['temp']))
#
# data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)

print(data['temp'].mean())
print(data['temp'].max())
print(data.condition)