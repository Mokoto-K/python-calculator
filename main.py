from gui import root

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
