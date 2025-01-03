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

# data = pandas.read_csv('weather_data.csv')
# print(data)
# print((data['temp']))
#
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)

# print(data['temp'].mean())
# print(data['temp'].max())
# print(data.condition)
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

import  pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
print(grey_squirrels_count)
print(black_squirrels_count)
print(cinnamon_squirrels_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirell_count.csv')