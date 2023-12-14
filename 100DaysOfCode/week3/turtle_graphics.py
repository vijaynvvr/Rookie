# from turtle import Turtle, Screen
# vj = Turtle()  # creating a turtle object
# vj.shape('turtle')
# vj.color('brown')
# # challenge: draw a sqauare with your turtle
# for i in range(4):
#     vj.forward(100)  # takes distance as argument, and goes that far
#     vj.right(90)  # takes angle as argument, and turns right by the amount of angle specified
# # screen = Screen()
# # screen.exitonclick()

# # types of importing
# # 1)
# import turtle
# a = turtle.Turtle()
#
# # 2)
# from turtle import Turtle
# b = Turtle()
#
# # 3) importing everything
# from turtle import *
# forward(100)  # no need of making an object of Turtle, since everything from turtle is imported
#
# # 4) aliasing modules
# import turtle as t
# c = t.Turtle()
#
# from turtle import Turtle as T
# d = T()
# d.forward(100)

# command for installing modules that are not part of python standard lirary:
# pip install module_name

# from turtle import Turtle, Screen
# import time
# vj = Turtle()
# for _ in range(15):
#     vj.forward(10)
#     vj.penup()
#     vj.forward(10)
#     vj.pendown()
#     time.sleep(.5)


# from turtle import Turtle
# from random import choice
# vj = Turtle()
# colours = ['red', 'black', 'orange', 'yellow', 'violet', 'blue', 'green', 'grey']
# for i in range(3, 11):
#     vj.color(choice(colours))
#     for j in range(i):
#         vj.forward(100)
#         vj.right(360/i)

# import turtle
# import random
# turtle.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rand_color = (r, g, b)
#     return rand_color
#
#
# vj = turtle.Turtle()
# directions = [0, 90, 180, 270]
# vj.pensize(15)
# vj.speed('fastest')
# for i in range(200):
#     vj.color(random_color())
#     vj.forward(30)
#     vj.right(choice(directions))


# import turtle
# from turtle import Turtle, Screen
# import random
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rand_color = (r, g, b)
#     return rand_color
#
#
# vj = Turtle()
# vj.speed('fastest')
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         vj.color(random_color())
#         vj.circle(100)
#         vj.setheading(vj.heading()+size_of_gap)
#
# draw_spirograph(1)
# Screen().exitonclick()


# import colorgram
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = list()
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# import random
# import turtle as t
# t.colormode(255)
# color_list = [(25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (226, 237, 228), (223, 137, 176), (144, 108, 56), (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50), (141, 208, 227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86), (98, 51, 36), (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161), (152, 213, 190), (242, 205, 8), (89, 48, 31)]
# vj = t.Turtle()
# vj.speed('fastest')
# vj.penup()
# vj.hideturtle()
# vj.setheading(225)
# vj.forward(300)
# vj.setheading(0)
# for i in range(10):
#     for j in range(10):
#         vj.dot(20, random.choice(color_list))  # though our pen is up, while drawing dot,
#         vj.forward(50)   # it will come down and go up again
#     vj.left(90)
#     vj.forward(50)
#     vj.setheading(180)
#     vj.forward(500)
#     vj.setheading(0)
#
# t.Screen().exitonclick()


# from selenium import webdriver
# chrome_driver_path = "C:\Development\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://www.cricbuzz.com/live-cricket-scores/35607/ind-vs-nz-final-icc-world-test-championship-final-2021")
# preview = driver.find_element_by_class_name("cb-com-ln ng-binding ng-scope cb-col cb-col-100")
# print(preview.text)
# driver.close()  # closes particular tab
# driver.quit()  # closes entire browser


# import turtle as t
# vj = t.Turtle()
# s = t.Screen()
#
#
# def move_forward():
#     vj.forward(30)
#
#
# t.listen()
# s.onkey(key='space', fun=move_forward)
# # here onkey is a higher order function, as it is taking another function as argument
# # and the function that goes as argument to  higher order function shouldn't have any arguments
# # usually this doesn't happen in other programming languages, but in py, we have higher order functions.
# s.exitonclick()


# import turtle as t
# vj = t.Turtle()
# s = t.Screen()
#
#
# def move_forwards():
#     vj.forward(10)
# def move_backwards():
#     vj.forward(10)
# def turn_let():
#     new_heading = vj.heading() + 10
#     vj.setheading(new_heading)
#     # alternate:
#     # vj.left(10)
# def turn_right():
#     new_heading = vj.heading() - 10
#     vj.setheading(new_heading)
#     # alternate:
#     # vj.right(10)
# def clear():
#     vj.clear()
#     vj.penup()
#     vj.home()
#     vj.pendown()
#
# t.listen()
# s.onkey(key='w', fun=move_forwards)
# s.onkey(key='s', fun=move_backwards)
# s.onkey(key='a', fun=turn_let)
# s.onkey(key='d', fun=turn_right)
# s.onkey(key='c', fun=clear)
# s.exitonclick()

from turtle import Turtle, Screen

screen = Screen()
screen.setup(400, 400)

turtle = Turtle()

turtle.penup()
turtle.goto(200, 200)
turtle.setheading(270)

for i in range(4):
    turtle.pendown()
    turtle.forward(400)
    turtle.right(90)

turtle.goto(190, 190)
turtle.setheading(270)
for i in range(4):
    turtle.forward(380)
    turtle.right(90)

turtle.goto(180, 180)
turtle.setheading(270)
for i in range(4):
    turtle.forward(360)
    turtle.right(90)


screen.exitonclick()
