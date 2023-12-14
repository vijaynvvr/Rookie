# import tkinter

# window = tkinter.Tk()  # to initialize a window (like Screen on turtle)
# window.title('My First GUI Program')  # title of the window
# window.minsize(width=500, height=300)  # window size setup

# # label:
# my_label = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))  # makes a label
# my_label.pack()  # packs the label on to the window # layouts the components on the window
# # my_label.pack(expand=(takes boolean),side=(takes: top, bottom, left or right))


# # holds the window on the screen(else window appears and disappears in a flash) like screen.exitonclick()
# window.mainloop()


# # functions with keyword or positional args:
# def my_fun(a, b, c):
#     # do this with a
#     # do this with b
#     # do this with c
# my_fun(1, 2, 3)  # positional args
# my_fun(b=2, c=3, a=1)  # keyword args
#
# # functions with default args:
# def my_fun(a = 0, b = 0, c = 0):
#     # do this with a
#     # do this with b
#     # do this with c
# my_fun(1, 3)  # a=1, b=3, c=0
# my_fun(b=2)  # a=0, b=2, c=0
# # when given default args, functions consider deault args when not given any value while calling the function


# # unlimited positional arguments:
# def add(*args):  # args is preferred by many programmers, we can actually use anything, ex: *nums
#     """can take any number of args and returns the sum of all values"""
#     sum_of_nums = 0
#     for i in args:  # args is a tuple
#         sum_of_nums += i
#     return sum_of_nums
# print(add(1, 2, 3, 4, 5))


# # unlimited keyword arguments
# def calculate(num, **kwargs):  # the keyword 'kwargs' is most preferred by developers, but you can use anything, ex: **kw
#     print(type(kwargs))  # kwargs is a dict class, whereas, args was tuple.
#     print(kwargs)
#     num += kwargs['add']
#     num *= kwargs['multiply']
#     return num
# print(calculate(5, add=5, multiply=3))
#
# class Car:
#     def __init__(self, **kw):
#         self.name = kw.get('name')
#         self.model = kw.get('model')
#         self.fuel_type = kw.get('fuel')
# car1 = Car(name='Maruti', model=800, fuel='Petrol')
# print(car1.model)
# car2 = Car(name='Hyundai')
# print(car2.fuel_type)  # we would get key error if we haven't used get() method for the dict


# from tkinter import *
# window = Tk()
# window.title('Still learning')
# window.minsize(height=400, width=600)

# # you can initialize attributes of a class in 3 ways:
# # 1) initialize while constructinng the object:
# my_label = Label(text='Yo guys', font=('Arial', 24, 'bold'))
# my_label.pack()
# # 2) set the value using dict concepts:
# my_label['text'] = 'yo yo guys'
# # 3) configure the object
# my_label.config(text='yo yo yo guys')

# # button

# def button_clicked():
#     print('I got clicked')
#     new_text = input.get() # to get hold of the string typed in the input box
#     my_label.config(text=new_text)

# button = Button(text='Click me', command=button_clicked)
# button.pack() # to pack the button on to the screen/window

# # entry (input box)

# input = Entry(width=25)
# input.pack()

# window.mainloop()


# from tkinter import *

# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)

# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()

# #Buttons
# def action():
#     print("Do something")

# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()

# #Entries
# entry = Entry(width=30)
# # Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()

# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()

# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()

# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# # radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# # radiobutton2.pack()ṇ

# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()


# from tkinter import *

# def button_clicked():
#     print('I got clicked')
#     my_text = inp.get()
#     my_label.config(text=my_text)

# window = Tk()
# window.title('My GUI')
# window.minsize(width=600, height=400)

# # Label
# my_label = Label(text='I am a label', font=('Courier', 24, 'bold'))
# my_label.config(text='I am a new label')
# # my_label.pack()
# my_label.grid(row=0, column=0)

# # Button
# button = Button(text='Click me', command=button_clicked)
# # button.pack()
# button.grid(row=1, column=2)

# # Entry
# inp = Entry(width=10)
# print(inp.get())
# # inp.place(x=500, y=300)
# inp.grid(row=2, column=0)

# # we can place our elements/widgets on to the window by 3 menthods:

# # 1) pack()
# # it just packs the elements on to the screen one below the other

# # 2) place(x=, y=) 
# # it is used to place the elements on the screen very precisely using the coordinates

# # 3) grid(row=, column=)
# # it is used to make the window into a grid system. Initially we need to specify row 
# # and column of an element at the top left, and then all of the other elements can be placed relative
# # to the first element.
# # and also, we cannot use grid and pack together 

# # padding:
# # you can configure the whole window or any particular widget with the padx and pady attributes
# # and change the padding around the widgets
# # example:
# window.config(padx=50, pady=50)
# my_label.config(padx=10, pady=10)

# window.mainloop()


# from tkinter import *
# window = Tk()
# window.title('canvas sample')
# window.config(padx=100, pady=50, bg='f7f5dd')  # background color for our window

# # canvas widget (allows us to lay things one on other)
# canvas = Canvas(width=200, height=224, bg='#f7f5dd', highlightthickness=0)  # we have a canvas on our window of width 200 and height 224
# # highlightthickness = 0 makes sure that the gap between the canvas and the windows or windows padding is 0
# # try removing highlightthickness and see the difference

# tomato_img = PhotoImage(file='tomato.png')  # storing an image
# # you can use './pomodoro-start/tomato.png' file path to access the image in the pomodoro-start folder
# # create_image() object cannot store immage directly with file path, so we use PhotoImage() object for appropriate image format

# canvas.create_image(100, 112, image=tomato_img)  # we are putting up an image on our canvas at specified coordinates
# # coordinates 100 and 112 are center of canvas, and we want to place our apple on center of the screen
# # you can adjust the coordinates of elements by trial and error on the canavas to make sure they are perfetctly placed

# canvas.create_text(100, 135, text='00:00', fill='white', font=('Courier', 35, 'bold'))  # we are putting up a text on our canvas at specified coordinates
# # coordinates 100 and 135 are adjusted on trail and error basis accordingly so that, the text appears on center of the image
# # fill attribute is used to specify the text colour

# canvas.pack() # packing our canvas on to the window

# window.mainloop()
