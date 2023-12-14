# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
# print(data)


# import _csv
# with open('weather_data.csv') as data_file:
#     data = _csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas
# data = pandas.read_csv('weather_data.csv')
# print(data['temp'])


# import pandas
# data = pandas.read_csv('weather_data.csv')

# # we have 2 primary data structures in pandas
# # 1) series ex: list of data (1-D)
# print(type(data['temp']))
# # 2) Dataframe ex: excel sheets (2-D)
# print(type(data))
#
# # conversion of dataframe:
# data_dict = data.to_dict()
# print(data_dict)
#
# # conversion of series:
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# # task: find the avg temperature:-
# temp_list = data['temp'].to_list()
# print(f'avg temp = {sum(temp_list)/len(temp_list)}')
# # easy alternative:
# print(f"avg temp = {data['temp'].mean()}")
#
# # task: find out max temperature:-
# max_temp = data['temp'].max()
# print(f'max temp = {max_temp}')
#
# # get data in columns:-
# print(data['condition'])
# # or
# print(data.condition)  # pandas automatically creates attribute of the column names which we can use

# # get data in rows:-
# print(data[data['day'] == 'Monday'])
# # or
# print(data[data.day == 'Monday'])

# # task: print the row of data having highest temperature
# highest_temp_row = data[data.temp == data.temp.max()]
# print(highest_temp_row)

# # accessing particular condition of a row
# monday = data[data.day == 'Monday']
# print(monday.condition)

# # task: convert monday's temperature to fahrenheit
# monday = data[data.day == 'Monday']
# monday_f_temp = 9/5 * int(monday.temp) + 32
# print(monday_f_temp)

# # create a dataframe from scratch:-
# data_dict = {
#     'students': ['vijay', 'vj', 'VJ'],
#     'scores': [99, 87, 96]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

import pandas
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
