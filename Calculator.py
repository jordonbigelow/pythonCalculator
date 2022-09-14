import math
from tkinter import *
from turtle import window_height, window_width

root = Tk()
root.title('Simple Calculator')
root.attributes('-alpha', 0.95)

window_width = 370
window_height = 455

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

screen_center_x = int((screen_width / 2) - (window_width / 2))
screen_center_y = int((screen_height / 2) - (window_height / 2))


root.geometry(
    f'{window_width}x{window_height}+{screen_center_x}+{screen_center_y}')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def buttonClick(number):
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + str(number))


def buttonClear():
    e.delete(0, END)


def buttonAdd():
    global first_num
    global math
    math = "addition"
    first_number = e.get()
    first_num = int(first_number)
    e.delete(0, END)


def buttonEquals():
    second_number = e.get()
    e.delete(0, END)
    # tests which arithmitic button was pressed
    if math == "addition":
        e.insert(0, first_num + int(second_number))
    if math == "subtraction":
        e.insert(0, first_num - int(second_number))
    if math == "multiplication":
        e.insert(0, first_num * int(second_number))
    if math == "division":
        e.insert(0, first_num / int(second_number))


def buttonSubtract():
    global first_num
    global math
    math = "subtraction"
    first_number = e.get()
    first_num = int(first_number)
    e.delete(0, END)


def buttonMultiply():
    global first_num
    global math
    math = "multiplication"
    first_number = e.get()
    first_num = int(first_number)
    e.delete(0, END)


def buttonDivide():
    global first_num
    global math
    math = "division"
    first_number = e.get()
    first_num = int(first_number)
    e.delete(0, END)


# Create number buttons
button_1 = Button(root, text="1", padx=41, pady=20,
                  command=lambda: buttonClick(1))
button_2 = Button(root, text="2", padx=40, pady=20,
                  command=lambda: buttonClick(2))
button_3 = Button(root, text="3", padx=40, pady=20,
                  command=lambda: buttonClick(3))
button_4 = Button(root, text="4", padx=40, pady=20,
                  command=lambda: buttonClick(4))
button_5 = Button(root, text="5", padx=40, pady=20,
                  command=lambda: buttonClick(5))
button_6 = Button(root, text="6", padx=40, pady=20,
                  command=lambda: buttonClick(6))
button_7 = Button(root, text="7", padx=40, pady=20,
                  command=lambda: buttonClick(7))
button_8 = Button(root, text="8", padx=40, pady=20,
                  command=lambda: buttonClick(8))
button_9 = Button(root, text="9", padx=40, pady=20,
                  command=lambda: buttonClick(9))
button_0 = Button(root, text="0", padx=39, pady=20,
                  command=lambda: buttonClick(0))

# Create unique buttons
button_add = Button(root, text="+", padx=39, pady=20, command=buttonAdd)
button_equals = Button(root, text="=", padx=101, pady=20, command=buttonEquals)
button_clear = Button(root, text="Clear", padx=89,
                      pady=20, command=buttonClear)
button_subtract = Button(root, text="-", padx=40,
                         pady=20, command=buttonSubtract)
button_multiply = Button(root, text="*", padx=41,
                         pady=20, command=buttonMultiply)
button_divide = Button(root, text="/", padx=42, pady=20, command=buttonDivide)

# Display buttons to the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=6, column=1, columnspan=2)
button_equals.grid(row=5, column=1, columnspan=2)
button_add.grid(row=5, column=0)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=4, column=1)
button_divide.grid(row=4, column=2)

root.mainloop()
