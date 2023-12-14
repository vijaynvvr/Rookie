from turtle import Turtle, Screen
import random

end_line = Turtle()
end_line.hideturtle()
end_line.color('cyan')
end_line.penup()
end_line.goto(360, 200)
end_line.setheading(270)
end_line.width(3)
end_line.pendown()
end_line.forward(400)

is_race_on = False
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['purple', 'red', 'blue', 'yellow', 'green', 'orange']
all_turtles = list()

for turtle_index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-370, y=-90 + 40 * turtle_index)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 350:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
