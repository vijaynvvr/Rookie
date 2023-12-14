# # simple function
# def greet(self):
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
# greet()

# # function that allows input
# def greetWithName(name):
#     print(f"Hello {name}.")
#     print(f"How do you do {name}?")
# greetWithName("Vijay")

# # functions with more than one input

# # positional arguments:
# def greetWith(name, location):
#     print(f"Hello {name}.")
#     print(f"How is it like in {location}?")
# greetWith("Vijay","Hyderabad")

# # keyword arguments:
# # we use parameter name of the function and assign argument values while calling the function
# def greetWith(name, location):
#     print(f"Hello {name}.")
#     print(f"How is it like in {location}?")
# greetWith(name = "Vijay", location = "Hyderabad")
# greetWith(location = "Hyderabad", name = "Vijay")
# # both of above statements output same shit

# # check For Prime:
# def checkForPrime(n):
#     isPrime = True
#     for i in range(2,n):
#         if n%i==0:
#             isPrime = False
#             break
#         else:
#             isPrime = True
#     if n==1:
#         print("Non Prime")
#     elif isPrime:
#         print("Prime")
#     else:
#         print("Non Prime")
# num = int(input("Enter the number: "))
# checkForPrime(num)

# # Caesar cipher:
# logo = """           
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
#             88             88                                 
#            ""             88                                 
#                           88                                 
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
# 8b         88 88       d8 88       88 8PP""""""" 88          
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
#               88                                             
#               88           
# """
# def caesar(startText, shiftAmount, cipherDirection):
#     endText = ""
#     for i in range(len(startText)):
#         if startText[i] in alphabet:
#             if cipherDirection == 'encode':
#                 Position = alphabet.index(startText[i])+shiftAmount
#                 while Position>25:
#                     Position -= 26
#                 endText += alphabet[Position]
#             elif cipherDirection == 'decode':
#                 Position = alphabet.index(startText[i])-shiftAmount
#                 if Position>25:
#                     Position += 26
#                 endText += alphabet[Position]
#         else:
#             endText += startText[i]
#     print(f"The {cipherDirection}d text is {endText}")
# print(logo) 
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# while True:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     caesar(startText = text, shiftAmount = shift, cipherDirection = direction)
#     if input("\nType 'yes' if you wanna go again. otherwise, give a 'no'.\n").lower() == 'no':
#         break
#     print("\n")

# #Dictionary:
# # empty dictionary:
# d = {}
# print(type(d))
# # adding new items to dictionary:
# d['name'] = 'vijay'
# d['age'] = 18
# print(d)
# # editing items in dictionary:
# d['age'] = 19
# print(d)
# # looping through dictionary to print key, value:
# for key in d:
#     print(key)
#     print(d[key])
# dict = {
#     'vijay': 'topper',
#     'virat': 'cricketer',
#     'vikas': 'daddu',
#     'marks': [1,2,3,65]
# }
# print(dict.keys()) #prints the keys of dictionary in dict_keys form
# print(list(dict.keys())) #prints the keys of dictionary in list form
# print(dict.values()) #prints the keys of dictionary in dict_values form
# print(list(dict.values())) #prints the keys of dictionary in list form
# print(dict.items()) #prints the (key,value) for all contents of dictionary in dict_items form
# updated_dict = {
#     'vj':'kacn',
#     'njc':'ahhcbj' 
# }
# dict.update(updated_dict) #updates the dictionary by adding key-value pairs from updated_dict
# print(dict['vj']) #prints value associated with 'vj'
# print(dict.get('vj')) #prints value associated with 'vj'
# # get() method is used to get rid of key error
# print(dict['vj2']) #returns an error as vj2 is not present in the
# print(dict.get('vj2')) #returns None as vj2 is not present in the dict

# # Given:
# studentScores = {
#     'Harry': 81,
#     'Hermione': 99,
#     'Ron': 78,
#     'Draco': 74,
#     'Neville': 62,
# }
# # Make a dictionary named studentGrades and grade the students accordingly:
# # 91-100 = Outstanding
# # 81-90 = Exceeds Expectations
# # 71-80 = Accepatable
# # 70 and below = Fail
# # Do not use any print statemet
# # Write your code: 
# studentGrades = {}
# for key in studentScores:
#     if studentScores[key] > 90:
#         studentGrades[key] = 'Outstanding'
#     elif studentScores[key] > 80:
#         studentGrades[key] = 'Exceeds Expectations'
#     elif studentScores[key] > 70:
#         studentGrades[key] = 'Acceptable'
#     elif studentScores[key] <= 70:
#         studentGrades[key] = 'Fail'
# # Given:
# print(studentGrades)

# # Nesting list in a dictionary
# travelLog = {
#     'France': ['Paris', 'Lille', 'Dijon'],
#     'Germany': ['Berlin', 'Hamburg', 'Stuttgart']
# }
# # Nesting dictionary in a dictionary
# travelLog = {
#     'France': {'citiesVisited': ['Paris', 'Lille', 'Dijon'], 'totalVisits': 12},
#     'Germany': {'citiesVisited': ['Berlin', 'Hamburg', 'Stuttgart'], 'totalVisits': 5}
# }
# # Nesting dictionary in a list
# travelLog = [
#     {
#         'country': 'France',
#         'citiesVisited': ['Paris', 'Lille', 'Dijon'], 
#         'totalVisits': 12
#     },
#     {
#         'country': 'Germany', 
#         'citiesVisited': ['Berlin', 'Hamburg', 'Stuttgart'], 
#         'totalVisits': 5
#     }
# ]

# # coding exercise:
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country, noOfVisits, citiesVisited):
#     newCountry = {
#         "country": country,
#         "visits": noOfVisits,
#         "cities": citiesVisited 
#     }
#     travel_log.append(newCountry)

# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# # Blind Auction:
# import os
# logo = '''
#                          ___________
#                          \\         /
#                           )_______(
#                           |"""""""|_.-._,.---------.,_.-._
#                           |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\\
#                        .-------------.
#                       /_______________\\
# '''
# print(logo)
# bids = {}
# def highest_bidder(biddingRecord):
#     maxBidValue = max(list(biddingRecord.values()))
#     for key in biddingRecord:
#         if biddingRecord[key] == maxBidValue:
#             return key
# while True:
#     name = input("What's your name? ")
#     price = int(input("What's your bid? $"))
#     bids[name] = price
#     if input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()=='yes':
#         os.system('cls')
#     else:
#         break
# print(f"Th winner is {highest_bidder(bids)}, with a bid of ${bids[highest_bidder(bids)]}.")

# def is_leap(year):
#   '''This is a docstring, which is used in explaining the functionality of a function.
#   Baically gives documentation about a function. Docstrings are declared just after the function
#   declaration with a given indentation. Try hovering over the function name. You'll see all this 
#   shit appearing as documentation.'''
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#     leap_month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year):
#         return leap_month_days[month-1]
#     else:
#         return month_days[month-1]

# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# # Calculator
# logo = """
#  _____________________
# |  _________________  |
# | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
# | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
# |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
# | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
# | |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
# | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |
# | |___|___|___| |___| | | |  \\ `.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ `.___.'\\  | |
# | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
# | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
# | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
# | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
# |_____________________|
# """
# # add
# def add(n1,n2):
#     return n1+n2
# # subtract
# def sub(n1,n2):
#     return n1-n2
# # multiply
# def mul(n1,n2):
#     return n1*n2
# # divide
# def div(n1,n2):
#     return n1/n2

# operations = {
#     '+': add,
#     '-': sub,
#     '*': mul,
#     '/': div
# }
# def calculator_recursive():
#     print(logo)
#     num1 = float(input("Enter the first number: "))
#     while True:
#         for symbol in operations:
#             print(symbol, end=', ')
#         print("\n", end='')
#         operation = input("Enter the operation from above list of operations: ")
#         num2 = float(input("Enter the next number: "))
#         function = operations[operation]
#         answer = function(num1,num2)
#         print(f"{num1} {operation} {num2} = {answer}")
#         choice = input(f"Do you wanna continue calculation calculating with {answer}? 'y' for yes and 'n' for new calculation and any other key to exit: ")
#         if choice == 'y':
#             num1 = answer
#         elif choice == 'n':
#             calculator_recursive()
#         else:
#             break
# calculator_recursive()

# # Blackjack Project:
# import random
# import os
# logo = """
# .------.            _     _            _    _            _    
# |A_  _ |.          | |   | |          | |  (_)          | |   
# |( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
# | \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# |  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
# `-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
#       |  \\/ K|                            _/ |                
#       `------'                           |__/           
# """
# def deal_card():
#       '''generates a random card from the deck of cards:'''
#       cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
#       card = random.choice(cards)
#       return card
# def calculate_score(cards):
#       '''calculates the total score of the deck of cards:'''
#       # a straight victory! a Blackjack.
#       if sum(cards) == 21 and len(cards) == 2: # 'is' operator and '==' operator are same
#             return 0
#       # the value of ace can be either 1 or 11 according to the situation, so if score
#       # is greater than 21, then ace will be 1, else, it will be 11
#       if 11 in cards and sum(cards) > 21:
#             cards.remove(11)
#             cards.append(1)
#       return sum(cards)
# def compare(user_score, computer_score):
#       if user_score == computer_score:
#             return "Draw."
#       elif computer_score == 0:
#             return "Lose, opponent has Blackjack."
#       elif user_score == 0:
#             return "Win with a Blackjack."
#       elif user_score > 21:
#             return "You went over, you lose."
#       elif computer_score > 21:
#             return "Opponent went over, you Win!."
#       elif user_score > computer_score:
#             return "User wins."
#       else:
#             return "You lose."
# def game_recursive():
#       user_cards = list()
#       computer_cards = list()
#       is_game_over = False
#       print(logo)
#       # adding 2 initial cards in user's and computer's deck:
#       for _ in range(2):
#             user_cards.append(deal_card())
#             computer_cards.append(deal_card())
#       while not is_game_over:
#             user_score = calculate_score(user_cards)
#             computer_score = calculate_score(computer_cards)
#             print(f"     Your cards: {user_cards}, current score: {user_score}")
#             print(f"     Computer's first card: {computer_cards[0]}")
#             print("\n")
#             if user_score == 0 or computer_score == 0 or user_score > 21:
#                   is_game_over = True 
#             else:
#                   user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
#                   if user_choice == 'y':
#                         user_cards.append(deal_card())
#                   else:
#                         is_game_over = True
#       while computer_score != 0 and computer_score < 17:
#             computer_cards.append(deal_card())
#             computer_score = calculate_score(computer_cards)
#       print(f"     Your final hand: {user_cards}, final score: {user_score}")
#       print(f"     Computer's final hand: {computer_cards}, final score: {computer_score}")
#       print("\n")
#       print(compare(user_score,computer_score))
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
#       os.system("cls")
#       game_recursive()

# # Scope:
# enemies = 1 # global variable
# def increase_enemies():
#       enemies = 2 # local variable given prefernce
#       print(f"Enemies inside function: {enemies}")
# increase_enemies()
# print(f"Enemies outside function: {enemies}")
# # Note: 1) global variables can be accessed from anywhere
# #       2) local variables can't be acccessed out of the local scope(block of code)
# #       3) blocks like if, elif, else, for, while wont create any local scope
# #       4) variables defined in functions are local, whereas, variables defined in blocks(if, loops etc) aren't local
# # to modify global variables, use 'global' keyword with the variable in local scope
# enemies = 'skeleton' # global variable
# def increase_enemies():
#       global enemies
#       enemies = 'zombies' # local variable given prefernce
#       print(f"Enemies inside function: {enemies}")
# increase_enemies()
# print(f"Enemies outside function: {enemies}")

# import random
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")
# difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
# compGuess = random.randint(1,100)
# guesses_remaining = 0
# if difficulty == 'easy':
#       guesses_remaining = 10
# elif difficulty == 'hard':
#       guesses_remaining = 5
# print(f"You have {guesses_remaining} attempts remaining to guess the number.")
# while guesses_remaining:
#       yourGuess = int(input("Make a guess: "))
#       if yourGuess > compGuess:
#             print("Too high.")
#             guesses_remaining -= 1
#       elif yourGuess < compGuess:
#             print("Too low.")
#             guesses_remaining -= 1
#       else:
#             print(f"You got it! The answer was {compGuess}")
#             break
#       print("Guess again.")
#       print(f"You have {guesses_remaining} attempts remaining to guess the number.")
# else:
#       print(f"You've run out of guesses, the correct number was {compGuess}, you lose.")

############DEBUGGING QUESTIONS#####################
# # 1) Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
# # 2) Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# # 3) Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# # 4) Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# # 5) Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# # 6) Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)
# mutate([1,2,3,5,8,13])
############DEBUGGING ANSWERS#####################
# # 1) Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
# # 2) Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])
# # 3) Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")
# # 4) Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#   print(f"You can drive at age {age}.")
# # 5) Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# # 6) Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)
# mutate([1,2,3,5,8,13])

# # 7) Question:
# number = int(input("Which number do you want to check?"))
# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")
# # 7) Answer:
# number = int(input("Which number do you want to check?"))
# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# # 8) Question:
# year = input("Which year do you want to check?")
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")
# # 8) Answer:
# year = int(input("Which year do you want to check?"))
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

# # 9) Question:
# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])
# # 9) Answer:
# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)