# from turtle import Turtle, Screen
# import selenium
# from my_module import my_var
# print(my_var)
# timmy = Turtle() #constructing an object named 'timmy' of class 'Turtle'
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# # installing  python packages
# # command to install PrettyTable: "pip install PrettyTable"
# from prettytable import PrettyTable
# table = PrettyTable()
# # add_column() is a method of the class: PrettyTable
# table.add_column('Pokemon Name', ['Pikachu', 'Squitle', 'Charmander'])
# table.add_column('Type', ['Electric', 'Water', 'Fire'])
# table.align = 'l' # aligns the table contents to left side, align is an attribute of the class: PrettyTable
# print(table)


# class user:
#     pass # we use pass if we dont have anything to write in body of a class or a funtion or in
#          # a loop or a conditional statement and we wanna get rid of indentaton error
# user_1 = user()

# # PascalCase, camelCase, snake_case
# # we use PascalCase for class names and snake_case for everything else, camelCase isnt much used in py

# # attribute: variable associated with the object
# user_1.id = '001'
# user_1.username = 'vijay'

# user_2 = user()
# user_2.id = '002'
# user_2.username = 'vj'

# # constructor is used to initialize objects with some attributes
# class User:
    
#     def __init__(self, user_id, username):
#         # initialize attributes
#         # init function is going to be called everytime we create a new object
#         self.id = user_id
#         self.username = username
#         self.followers = 0

# # constructor can help reduce the code as we are constructing the objects with atributes

# user_1 = User('001', 'vijay')
# user_2 = User('002', 'vj')

# # now every time we create an object of class 'User', we must initialize or construct the
# # object with the attributes 'id' and 'username'.
# # You need not construct your object with the followers attribute, coz its a default attribute
# # Once, a constructor (__init__ method) is defined, the object needs to be initialized with
# # the attributes present in the __init__ method.

# user_3 = User() # this gives an error as the object lacks two positional arguments


# class InstaUser:
    
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
    
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1

# user1 = InstaUser('001', 'vijay')
# user2 = InstaUser('002', 'vj')
# user1.follow(user2)
# print(user1.followers)
# print(user1.following)
# print(user2.followers)
# print(user2.following)