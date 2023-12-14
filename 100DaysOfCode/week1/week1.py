# # even or odd
# num = int(input("Enter a number: "))
# if num%2:
#     print("Odd")
# else:
#     print("Even")

# # bmi calci
# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
# bmi = round(weight/height**2)
# if bmi < 18.5:
#     print(f"Your bmi is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your bmi is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your bmi is {bmi}, you are overweight.")
# elif bmi < 35:
#     print(f"Your bmi is {bmi}, you are obese.")
# else:
#     print(f"Your bmi is {bmi}, you are clinically obese.")

# # leap year
# year = int(input("Enter the year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year.")
# else:
#     print("Not a leap year.")

# # small pizza = $15
# # medium pizza = $20
# # large pizza = $25
# # pepperoni for small pizza = +$2
# # pepperoni for medium pizza or large pizza = +$3
# # Extra cheese for any pizza = +$1
# # print total bill
# print("Welcome to Python Pizza Deliveries")
# size = input("What size pizza do you want? S, M or L? ")
# add_pepperant = input("Do you want pepperant? Y or N? ")
# extra_cheese = input("Do you want extra cheese? Y or N? ")
# bill = 0
# if size == "S":
#     bill += 15
#     if add_pepperant == "Y":
#         bill += 2
#     if extra_cheese == "Y":
#         bill += 1
# elif size == "M":
#     bill += 20
#     if add_pepperant == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
# else:
#     bill += 25
#     if add_pepperant == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
# print(f"Your final bill is: ${bill}")

# #Love Calculator
# print("Welcome to the Love Calculator!")
# name1 = input("Enter your name: ")
# name2 = input("Enter their name: ")
# lower_name1 = name1.lower()
# lower_name2 = name2.lower()
# T = lower_name1.count('t') + lower_name2.count('t')
# R = lower_name1.count('r') + lower_name2.count('r')
# U = lower_name1.count('u') + lower_name2.count('u')
# E = lower_name1.count('e') + lower_name2.count('e')
# TRUE = T + R + U + E
# L = lower_name1.count('l') + lower_name2.count('l')
# O = lower_name1.count('o') + lower_name2.count('o')
# V = lower_name1.count('v') + lower_name2.count('v')
# E = lower_name1.count('e') + lower_name2.count('e')
# LOVE = L + O + V + E
# Love_score = str(TRUE) + str(LOVE)
# Love_score = int(Love_score)
# if (Love_score < 10) or (Love_score > 90):
#     print(f"Your love score is {Love_score}, you go together like coke and mentos.")
# elif (Love_score >= 40) and (Love_score <= 50):
#     print(f"Your love score is {Love_score}, you are alright together.")
# else:
#     print(f"Your love score is {Love_score}.")

# # Treasure Island
# print("Welcome to Treasure Island.")
# print("Your misison is to find the Treasure.")
# choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right". \n').lower()
# if choice1 == "left":
#     choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
#     if choice2 == "wait":
#         choice3 = input("You arrive at an island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
#         if choice3 == "red":
#             print("It's a room full of fire, Game Over.")
#         elif choice3 == "yellow":
#             print("You found the Treasure! You Win!!!")
#         elif choice3 == "blue":
#             print("It's a room full of beasts, Game Over.")
#         else:
#             print("You chose a door that doesn't exists, Game Over.")
#     else:
#         print("You got attacked by a crocodile, Game Over.")
# else:
#     print("You fell into a hole, Game Over.")

# # Toss generator
# import random

# rand = random.randint(0,1)
# if rand:
#     print("Heads")
# else:
#     print("Tails")

# # lists
# states = ["ap", "telangana", "orissa"]
# states.append("punjab")
# states.extend(["karnataka", "gujrat"])
# # states.clear()
# print(states)

# # bill payer
# import random
# names = input("Give me everybody's names, separated by a comma. \n").split(", ")
# print(f"{names[random.randint(0, len(names)-1)]} will pay the bill.")

# # nesting of lists
# fruits = ["apple", "banana"]
# vegetables = ["tomato", "potato"]
# eatables = [fruits, vegetables]
# print(eatables[1][0])

# # Rock Paper Scissors
# Rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """

# Paper = """
#      _______
# ---'    ____)____
#            ______)
#           ________)
#          _______)
# ---.__________)
# """

# Scissors = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """
# import random
# print("ROCK PAPER SCISSORS")
# print("Rock wins over Scissors, Scissors wins over Paper, Paper wins over Rock.")
# you = int(input("Enter \"1\" for Rock, \"2\" for Paper, \"3\" for Scissors: "))
# comp = random.randint(1,3)
# if (you == 1):
#     print("You chose:")
#     print(Rock)
#     if (comp == 1):
#         print("Comp chose:")
#         print(Rock)
#         print("It's a draw.")
#     elif (comp == 2):
#         print("Comp chose:")
#         print(Paper)
#         print("You lost.")
#     else:
#         print("Comp chose:")
#         print(Scissors)
#         print("You won.")
# elif (you == 2):
#     print("You chose:")
#     print(Paper)
#     if (comp == 1):
#         print("Comp chose:")
#         print(Rock)
#         print("You won.")
#     elif (comp == 2):
#         print("Comp chose:")
#         print(Paper)
#         print("It's a draw.")
#     else:
#         print("Comp chose:")
#         print(Scissors)
#         print("You lost.")
# elif (you == 3):
#     print("You chose:")
#     print(Scissors)
#     if (comp == 1):
#         print("Comp chose:")
#         print(Rock)
#         print("You lost.")
#     elif (comp == 2):
#         print("Comp chose:")
#         print(Paper)
#         print("You won.")
#     else:
#         print("Comp chose:")
#         print(Scissors)
#         print("It's a draw.")
# else:
#     print("You lost as you entered an invalid number.")

# # for loop:
# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(fruit)

# # Average height using for loop:
# heights = input("Enter student heights: ").split()
# for n in range(0, len(heights)):
#     heights[n] = int(heights[n])
# sum = 0
# for n in heights:
#     sum += n
# num = 0
# for n in heights:
#     num += 1
# print(f"Average height is {round(sum/num)}.")

# # Highest score using for loop:
# scores = input("Enter student scores: ").split()
# for n in range(0, len(scores)):
#     scores[n] = int(scores[n])
# max = scores[0]
# for score in scores:
#     if (score > max):
#         max = score
# print(f"Maximum score is {max}.")

# # print first 10 natural numbers
# for num in range( 1,11):
#     print(num)

# # print even numbers below 10
# for num in range(2, 10, 2):
#     print(num)

# # print sum of first 100 natural numbers
# sum = 0
# for num in range(1,101):
#     sum += num
# print(sum)

# # print 2+4+6+8+10+......+98+100
# sum = 0
# for num in range(2,101,2):
#     sum += num
# print(sum)

# # FizzBuzz: Popular interview question
# # print "Fizz" if number is divisible by 3
# #       "Buzz" if number is divisible by 5
# #       "FizzBuzz" if number is divisible by both 3 and 5
# #       and print the number itself if none of the conditions satisfy
# for num in range(1,101):
#     if (num%3==0 and num%5==0):
#         print("FizzBuzz")
#     elif (num%3==0):
#         print("Fizz")
#     elif (num%5==0):
#         print("Buzz")
#     else:
#         print(num)

# # Easy level password generator
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print("Welcome to the PyPassword Genertor!")
# nr_letters = int(input("How many letters would you like in your paassword?\n"))
# nr_symbols = int(input("How many symbols would you like?\n"))
# nr_numbers = int(input("How many numbers would you like?\n"))
# paassword = ""
# for char in range(1, nr_letters+1):
#     paassword += letters[random.randint(0, 51)]
# for char in range(1, nr_symbols+1):
#     paassword += symbols[random.randint(0, 9)]
# for char in range(1, nr_numbers+1):
#     paassword += numbers[random.randint(0, 9)]
# print(f"Your password is {paassword}.")

# # Hard level password generator
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print("Welcome to the PyPassword Genertor!")
# nr_letters = int(input("How many letters would you like in your paassword?\n"))
# nr_symbols = int(input("How many symbols would you like?\n"))
# nr_numbers = int(input("How many numbers would you like?\n"))
# paassword_list = []
# for char in range(1, nr_letters+1):
#     paassword_list += letters[random.randint(0, 51)]
# for char in range(1, nr_symbols+1):
#     paassword_list += symbols[random.randint(0, 9)]
# for char in range(1, nr_numbers+1):
#     paassword_list += numbers[random.randint(0, 9)]
# random.shuffle(paassword_list)
# paassword = ""
# for char in paassword_list:
#     paassword += char
# print(f"Your password is {paassword}.")

# # function demonstration:
# def greet_me(name):
#     print("Hello " + name + "!")
# name = input("Enter your name: ")
# greet_me(name)

# list  = [1, 2.4, "cbit"]
# print(list)

# # Hangman
# import random
# import os
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# logo = ''' 
#  _                                             
# | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                    |___/    '''
# wordList = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack',
#             'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie']
# def printList(l):
#     for i in l:
#         print(i,end=' ')
#     print("\n")
# chosenWord = random.choice(wordList)
# Display = list()
# for i in range(len(chosenWord)):
#     Display.append("_")
# lives = 6
# print(logo)
# while '_' in Display and lives != 0:
#     guess = input("Guess a letter: ").lower()
#     os.system("cls")
#     print(logo)
#     if guess in Display:
#         print(f"\nYou've already guessed {guess}.\n")
#     for i in range(len(chosenWord)):
#         if guess == chosenWord[i]:
#             Display[i] = guess
#     printList(Display)
#     if guess not in chosenWord:
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
#         lives -= 1
#     print(stages[lives])
#     if lives == 0:
#         print(f"You Lose. The word is {chosenWord}.")
#         break
# else:
#     print("You Win.")