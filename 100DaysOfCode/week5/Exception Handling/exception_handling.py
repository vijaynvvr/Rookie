# # FileNotFound
# with open('a_file.txt') as file:  # there is no such 'a_file.txt' in present working directory 
#     file.read()

# # KeyError  # key not present in the dictionary
# a_dict = {'key': 'value'}
# value = a_dict['non_existent_key']

# # IndexError  # when index out of range
# fruit_list = ['Apple', 'Banana', 'Mango']
# fruit = fruit_list[3]

# # TypeError  # you can't concatenate a string and an integer
# text = 'abc'
# print(text + 3)

# # NameError  # when you use variables without declaring them
# a = 2
# print(c)

# # ZeroDivisionError
# a = 1
# print(a/0)

# # ValueError
# a = int(input('Enter an integer: '))
# # now if an input other than integer is given, the it is a value error


# try: 
#     # something that might cause an exception
#     pass

# except:
#     # do this if there was an exception
#     pass

# else:
#     # do this if there were no exceptions
#     pass

# finally:
#     # do this no matter what happens
#     pass


# try:
#     file = open('a_file.txt')
# except:
#     file = open('a_file.txt', 'w')
#     file.write('Something')


# # Like above, never use bare except
# try:
#     file = open('a_file.txt')  # FileNotFoundError
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['dabididibide'])  # KeyError
# except FileNotFoundError:  # instead use multiple except blocks with error names
#     file = open('a_file.txt', 'w')
#     file.write('Something')
# except KeyError as error_message :  # we are defining exceptions separately for different errors 
#                   # instead of defining only one except block for all the errors like last snippet
#     print(f'That key {error_message} does not exist')
# else:  # if there are no errors in try block, then else block is triggered
#        # if there are any errors, then else is never triggered, instead, except block is triggered accordingly
#     content = file.read()
#     print(content)
# finally:  # this block of code is gonna run no matter what happens
#           # so finally is not often used 
#     file.close()
#     print('File was closed')
#     raise TypeError('Ntg bro, I just felt like raising an exception 🤡')


# # raising exceptions:
# height = float(input('Height: '))
# weight = int(input('Weight: '))

# if height > 3:
#     raise ValueError('Human Height should not be over 3 meters.')

# bmi = weight / height ** 2
# print(bmi)


# # Q: Use what you've learnt about exception handling to prevent the program from crashing.
# # If the user enters something that is out of range just print a default output of "Fruit pie"
# fruits = ["Apple", "Pear", "Orange"]

# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")

# make_pie(4)

# # Ans:
# fruits = ["Apple", "Pear", "Orange"]

# def make_pie(index):
    
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print('Fruit pie')
#     else:
#         print(fruit + " pie")
    
# make_pie(4)


# # Q: You'll need to catch the KeyError exception. Posts without any likes can be counted as 0 likes.
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]

# total_likes = 0

# for post in facebook_posts:
#     total_likes = total_likes + post['Likes']

# print(total_likes)

# # Ans:
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]

# total_likes = 0

# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass
#         # or
#         # total_likes += 0
    
# print(total_likes)
