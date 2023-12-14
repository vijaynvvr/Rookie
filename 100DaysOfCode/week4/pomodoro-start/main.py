from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title.config(text='Timer')
    check_marks.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    # 25 min work, 5 min short break,
    # 25 min work, 5 min short break,
    # 25 min work, 5 min short break,
    # 25 min work, 20 min long break 
    
    if reps%8 == 0:
        # if it is 8th rep:
        title.config(text='Break', fg=RED)
        count_down(long_break_sec)
    elif reps%2 == 0:
        # if it is 2nd/4th/6th rep:
        title.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    else:
        # if it is 1st/3rd/5th/7th rep:
        title.config(text='Work', fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count//60
    count_sec = count%60
    if count_sec < 10:
        count_sec = f'0{count_sec}'  # formatting count_sec in a better way
    # python is a strongly, dynamically typed language
    # datatype of variable gets changed dynamically according to the value we put in the variable 

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    # the above method is used to configure items on canvas
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        # after is used to repeat certain task(function) after some milli seconds(1000 in this case, which 1sec)
        # and after each iteration, the task that needs to be done (count - 1 in this case)   
    else:
        start_timer()
        marks = ''
        for i in range(reps//2):
            marks += '✔'
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50,))
# fg: colour of the text
# bg: colour of background
title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1) 

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check_marks.grid(row=3, column=1)

window.mainloop()
# constantly loops to detect if stg happens on the screen, as this is a GUI.
