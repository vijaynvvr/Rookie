from tkinter import *
from typing import Collection

window_bg = 'violet'
label_bg = 'violet'

window = Tk()
window.title('Miles to Kilometer Converter')
window.config(padx=30, pady=30, background=window_bg)

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_value_label.config(text=f'{km}')

miles_input = Entry(width=5)
miles_input.grid(row=0, column=1)

miles_label = Label(text='Miles', font=('Times New Roman', 20, 'bold'))
miles_label.config(background=label_bg)
miles_label.grid(row=0, column=2)

equal_to_label = Label(text='is equal to :', font=('Times New Roman', 20, 'bold'))
equal_to_label.config(background=label_bg)
equal_to_label.grid(row=1, column=0)

km_value_label = Label(text='0', font=('Times New Roman', 20, 'bold'))
km_value_label.config(background=label_bg)
km_value_label.grid(row=1, column=1)

km_label = Label(text='Km', font=('Times New Roman', 20, 'bold'))
km_label.config(background=label_bg)
km_label.grid(row=1, column=2)

calculate_button = Button(text='Calculate', command=miles_to_km, font=('Times New Roman', 10, 'bold'))
calculate_button.config(background='yellow')
calculate_button.grid(row=2, column=1)

window.mainloop()