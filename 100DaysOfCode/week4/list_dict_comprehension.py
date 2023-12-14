# # usually, we write long codes for lists and dictionary operations, but with list comprehension, life is easy.
#
# numbers = [1, 2, 3]
# new_list = []
# for num in numbers:
#     new_num = num + 1
#     new_list.append(new_num)
# print(new_list)


# # by list comprehension: new_list = [new_item for item in list]
#
# numbers = [1, 2, 3]
# new_list = [num + 1 for num in numbers]


# # write a code to convert a string to list of characters
# string = input('Enter a string: ')
# list_of_chars = [char for char in string]
# # or
# # list_of_chars = list(string)
# print(list_of_chars)


# # list comprehension with condition
# # new_list = [new_item for item in list if condition]
# # new_item gets added to the new_list only when condition is True
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
# # make a new list with names of char length less than or equal to 4:
# new_names = [name for name in names if len(name) <= 4]
# print(new_names)
# # create a new list that contains the names longer than 5 chars in ALL CAPS
# CAP_names = [name.upper() for name in names if len(name) > 5]
# print(CAP_names)


# dictionary comprehension:
# new_dict = {new_ke: new_value for item in list}
# or
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# or
# new_dict = {new_key: new_value for (key, value) in dict.items() if condition}


# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
# # create a dict with key as name and value as a random score:
# students_scores = {name: random.randint(1, 100) for name in names}
# # create a dict who scored greater than 60:
# passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day: round(9/5 * cel + 32, 1) for (day, cel) in weather_c.items()}
# print(weather_f)


import pandas
# looping through dataframes:
student_dict = {
    "students": ['Vijay', 'vj', 'VJ'],
    "scores": [99, 97, 98]
}
student_data_frame = pandas.DataFrame(student_dict)
# loop through rows of a dataframe:
for (index, row) in student_data_frame.iterrows():
    # can print index:
    print(index)
for (index, row) in student_data_frame.iterrows():
    # can print row:
    print(row)
for (index, row) in student_data_frame.iterrows():
    # can print student names:
    print(row.students)
for (index, row) in student_data_frame.iterrows():
    # can print student scores:
    print(row.scores)
