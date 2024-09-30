from tkinter import Tk, StringVar, messagebox  # , PhotoImage
from tkinter import ttk

# TODO - Fix resizing of gui
# TODO - Fix rounding behaviour
# TODO - Fix double operator behaviour i.e ++, /*, etc

EQUATION = ""


def equation(num: str):
    global EQUATION

    if len(EQUATION) < 12:
        EQUATION += num

    screen.set(EQUATION)
    return EQUATION


def equals():
    global EQUATION

    if EQUATION.startswith(")"):
        return
    elif EQUATION != "":
        try:
            evaluate = eval(EQUATION)
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


# Main Gui config
mainframe = ttk.Frame(root, padding=2)  # , padding=(2, 2, 2, 2)
mainframe.grid(column=0, row=0, sticky="NSEW")


# Calculator screen config
screen: StringVar = StringVar()
screen_label = ttk.Label(mainframe, padding=2, text=EQUATION, textvariable=screen, font=("Arial", 70, "bold"))
screen_label.grid(column=0, row=0, sticky="NSEW", columnspan=4, rowspan=2)

# Power, reset, del buttons
reset_button: ttk.Button = ttk.Button(mainframe, text="RESET", command=reset)
reset_button.grid(column=0, row=2, sticky="NSEW", columnspan=2)

delete_button: ttk.Button = ttk.Button(mainframe, text="DELETE", command=delete)
delete_button.grid(column=2, row=2, sticky="NSEW", columnspan=2)

power_button: ttk.Button = ttk.Button(mainframe, text="OFF", command=exit)
power_button.grid(column=4, row=2, sticky="NSEW")

# Number buttons
number_font = ("Arial", 20, "bold")
number_padding = 0, 0

one_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="1", command=lambda: equation("1"))
one_button.grid(column=0, row=3, sticky="NSEW")

two_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="2", command=lambda: equation("2"))
two_button.grid(column=1, row=3, sticky="NSEW")

three_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="3", command=lambda: equation("3"))
three_button.grid(column=2, row=3, sticky="NSEW")

four_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="4", command=lambda: equation("4"))
four_button.grid(column=0, row=4, sticky="NSEW")

five_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="5", command=lambda: equation("5"))
five_button.grid(column=1, row=4, sticky="NSEW")

six_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="6", command=lambda: equation("6"))
six_button.grid(column=2, row=4, sticky="NSEW")

seven_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="7", command=lambda: equation("7"))
seven_button.grid(column=0, row=5, sticky="NSEW")

eight_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="8", command=lambda: equation("8"))
eight_button.grid(column=1, row=5, sticky="NSEW")

nine_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="9", command=lambda: equation("9"))
nine_button.grid(column=2, row=5, sticky="NSEW")

zero_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="0", command=lambda: equation("0"))
zero_button.grid(column=0, row=6, sticky="NSEW", columnspan=3)

# Operation buttons

addition_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="+", command=lambda: equation("+"))
addition_button.grid(column=3, row=3, sticky="NSEW")

subtraction_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="-", command=lambda: equation("-"))
subtraction_button.grid(column=4, row=3, sticky="NSEW")

multiply_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="x", command=lambda: equation("*"))
multiply_button.grid(column=3, row=4, sticky="NSEW")

division_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="/", command=lambda: equation("/"))
division_button.grid(column=4, row=4, sticky="NSEW")

left_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="(", command=lambda: equation("("))
left_button.grid(column=3, row=5, sticky="NSEW")

right_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text=")", command=lambda: equation(")"))
right_button.grid(column=4, row=5, sticky="NSEW")

equals_button: ttk.Button = ttk.Button(mainframe, padding=number_padding, text="=", command=equals)
equals_button.grid(column=3, row=6, sticky="NSEW", columnspan=2)


root.grid_columnconfigure(0, weight= 1)
mainframe.grid_columnconfigure(0, weight= 1)
mainframe.grid_columnconfigure(1, weight= 1)
mainframe.grid_columnconfigure(2, weight= 1)
mainframe.grid_columnconfigure(3, weight= 1)
mainframe.grid_columnconfigure(4, weight= 1)

root.grid_rowconfigure(0, weight=1)
mainframe.grid_rowconfigure(0, weight=1)
mainframe.grid_rowconfigure(1, weight=1)
mainframe.grid_rowconfigure(2, weight=1)
mainframe.grid_rowconfigure(3, weight=1)
mainframe.grid_rowconfigure(4, weight=1)
mainframe.grid_rowconfigure(5, weight=1)
mainframe.grid_rowconfigure(6, weight=1)

# --------------- Calculator functionality -----------------


# def addition(a: float, b: float) -> float:
#     return a + b
#
#
# def subtraction(a: float, b: float) -> float:
#     return a - b
#
#
# def multiplication(a: float, b: float) -> float:
#     return a * b
#
#
# def division(a: float, b: float) -> float:
#     if b != 0:
#         return a / b
#     else:
#         print("Cannot divide by zero")
#
#
# def calculation(a: float, b: float, operation: str) -> float:
#     if operation == "+":
#         return addition(a, b)
#     elif operation == "-":
#         return subtraction(a, b)
#     elif operation == "*":
#         return multiplication(a, b)
#     elif operation == "/":
#         return division(a, b)
#     else:
#         print("Something went wrong, try again")
#
#
# def get_user_number() -> float:
#     while True:
#         try:
#             number: float = float(input("Enter a number: "))
#         except ValueError:
#             print(f"Please enter an integer or float value")
#         else:
#             return number
#
#
# def get_user_operation() -> str:
#     operations: list[str] = ['+', '-', '*', '/']
#
#     while True:
#         users_input: str = input("Enter an operation, '+', '-', '*' or '/': ")
#         if users_input in operations:
#             return users_input
#         else:
#             print(f"{users_input} is not a valid operation, please enter either '+', '-', '*' or '/'")
#
#
# def run_again() -> bool:
#     while True:
#         calculate_again = input("Would you like to do another calculation, 'Yes' or 'No': ").lower()
#         if calculate_again == "yes":
#             return True
#         elif calculate_again == "no":
#             print("Thank you for mathing with me")
#             return False
#         else:
#             print(f"{calculate_again} is not a valid answer, please type 'Yes' or 'No'")


# Main entry point for our program
def main() -> None:

    root.mainloop()
    # do_math: bool = True
    # while do_math:
    #     number_1: float = get_user_number()
    #     operation: str = get_user_operation()
    #     number_2: float = get_user_number()
    #     print(calculation(number_1, number_2, operation)) # NOQA
    #     do_math = run_again()


if __name__ == "__main__":
    main()
