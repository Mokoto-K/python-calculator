from tkinter import Tk, StringVar, messagebox  # , PhotoImage
from tkinter import ttk

# TODO - Fix rounding behaviour
# TODO - Fix double operator behaviour i.e ++, /*, etc

EQUATION = ""

# ---------------Functionality----------------

def equation(num: str):
    global EQUATION

    if len(EQUATION) < 20:
        EQUATION += num

    screen.set(EQUATION)
    return EQUATION


def do_math():
    global EQUATION

    if EQUATION.startswith(")"):
        return
    elif EQUATION != "":
        try:
            evaluate = round(eval(EQUATION), 4)
            screen.set(str(evaluate))
            EQUATION = str(evaluate)
        except ZeroDivisionError:
            messagebox.showerror("Error", "You can't divide by 0")
        except SyntaxError:
            messagebox.showerror("Error", "You forgot to close the brackets")


def reset() -> str:
    global EQUATION
    EQUATION = ""
    screen.set(EQUATION)
    return EQUATION


def delete() -> str:
    global EQUATION
    EQUATION = EQUATION[:-1]
    screen.set(EQUATION)
    return EQUATION


root = Tk()
root.title("Python Calculator")
root.geometry("800x500")

#-----------------------GUI Elements-----------------------

# Main Gui config
mainframe = ttk.Frame(root, padding=(2, 2, 2, 2))
mainframe.grid(column=0, row=0, sticky="NSEW")

# Screen only frame
screenframe = ttk.Frame(mainframe, padding=2)
screenframe.grid(column=0, row=0, sticky="NSEW")

# button only frame
buttonframe = ttk.Frame(mainframe, padding=2)
buttonframe.grid(column=0, row=1, sticky="NSEW")

# Calculator screen config
screen: StringVar = StringVar()
screen_label = ttk.Label(screenframe, padding=2, text=EQUATION, textvariable=screen, font=("Arial", 50, "bold"))
screen_label.grid(column=0, row=0, sticky="NSEW", columnspan=5, rowspan=2)

# Power, reset, del buttons
reset_button: ttk.Button = ttk.Button(buttonframe, text="RESET", command=reset)
reset_button.grid(column=0, row=0, sticky="NSEW", columnspan=2)

delete_button: ttk.Button = ttk.Button(buttonframe, text="DELETE", command=delete)
delete_button.grid(column=2, row=0, sticky="NSEW", columnspan=2)

power_button: ttk.Button = ttk.Button(buttonframe, text="OFF", command=exit)
power_button.grid(column=4, row=0, sticky="NSEW")

# Number buttons
number_font = ("Arial", 20, "bold")
number_padding = 0, 0

one_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="1", command=lambda: equation("1"))
one_button.grid(column=0, row=1, sticky="NSEW")

two_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="2", command=lambda: equation("2"))
two_button.grid(column=1, row=1, sticky="NSEW")

three_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="3", command=lambda: equation("3"))
three_button.grid(column=2, row=1, sticky="NSEW")

four_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="4", command=lambda: equation("4"))
four_button.grid(column=0, row=2, sticky="NSEW")

five_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="5", command=lambda: equation("5"))
five_button.grid(column=1, row=2, sticky="NSEW")

six_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="6", command=lambda: equation("6"))
six_button.grid(column=2, row=2, sticky="NSEW")

seven_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="7", command=lambda: equation("7"))
seven_button.grid(column=0, row=3, sticky="NSEW")

eight_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="8", command=lambda: equation("8"))
eight_button.grid(column=1, row=3, sticky="NSEW")

nine_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="9", command=lambda: equation("9"))
nine_button.grid(column=2, row=3, sticky="NSEW")

zero_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="0", command=lambda: equation("0"))
zero_button.grid(column=0, row=4, sticky="NSEW", columnspan=3)

# Operation buttons

addition_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="+", command=lambda: equation("+"))
addition_button.grid(column=3, row=1, sticky="NSEW")

subtraction_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="-", command=lambda: equation("-"))
subtraction_button.grid(column=4, row=1, sticky="NSEW")

multiply_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="x", command=lambda: equation("*"))
multiply_button.grid(column=3, row=2, sticky="NSEW")

division_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="/", command=lambda: equation("/"))
division_button.grid(column=4, row=2, sticky="NSEW")

left_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="(", command=lambda: equation("("))
left_button.grid(column=3, row=3, sticky="NSEW")

right_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text=")", command=lambda: equation(")"))
right_button.grid(column=4, row=3, sticky="NSEW")

equals_button: ttk.Button = ttk.Button(buttonframe, padding=number_padding, text="=", command=do_math)
equals_button.grid(column=3, row=4, sticky="NSEW", columnspan=2)


root.grid_columnconfigure(0, weight= 1)
mainframe.grid_columnconfigure(0, weight= 1)
screenframe.grid_columnconfigure(0, weight= 1)
buttonframe.grid_columnconfigure(0, weight= 1)
buttonframe.grid_columnconfigure(1, weight= 1)
buttonframe.grid_columnconfigure(2, weight= 1)
buttonframe.grid_columnconfigure(3, weight= 1)
buttonframe.grid_columnconfigure(4, weight= 1)

root.grid_rowconfigure(0, weight=1)
mainframe.grid_rowconfigure(0, weight=1)
mainframe.grid_rowconfigure(1, weight=10)
screenframe.grid_rowconfigure(0, weight=1)
buttonframe.grid_rowconfigure(0, weight=1)
buttonframe.grid_rowconfigure(1, weight=1)
buttonframe.grid_rowconfigure(2, weight=1)
buttonframe.grid_rowconfigure(3, weight=1)
buttonframe.grid_rowconfigure(4, weight=1)
