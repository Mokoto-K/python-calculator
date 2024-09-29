def addition(*numbers: float) -> float:
    total = 0
    for number in numbers:
        total += number
    return total


def subtraction(*numbers: float) -> float:
    total = 0
    for number in numbers:
        total -= number
    return total


def multiplication(*numbers: float) -> float:
    total = 0
    for number in numbers:
        total *= number
    return total


def division(*numbers: float) -> float:
    total = 0
    for number in numbers:
        total /= number
    return total


def calculation(a: float, b: float, operation: str) -> float:
    if operation == "+":
        return addition(a, b)
    elif operation == "-":
        return subtraction(a, b)
    elif operation == "*":
        return multiplication(a, b)
    elif operation == "/":
        return division(a, b)
    else:
        return f"{operation} is not a valid operation, please enter either '+', '-', '*' or '/'" # NOQA



# Main entry point for our program
def main() -> None:

    do_math: bool = True
    while do_math:

        control: int = 0
        while control == 0:
            try:
                number_1: float = float(input("Enter a number: "))
                control = 1
            except ValueError:
                print(f"Please enter an integer or float value")

        operation: str = input("Enter an operation, '+', '-', '*' or '/': ")

        while control == 1:
            try:
                number_2: float = float(input("Enter another number: "))
                control = 0
            except ValueError:
                print(f"Please enter an integer or float value")

        print(calculation(number_1, number_2, operation)) # NOQA

        calculate_again: str = " "

        while calculate_again != "yes" or calculate_again != "no":
            calculate_again = input("Would you like to do another calculation, 'Yes' or 'No'").lower()

            if calculate_again == "yes":
                break
            elif calculate_again == "no":
                print("Thank you for mathing with me")
                do_math = False
                break
            else:
                print(f"{calculate_again} is not a valid answer, please type 'Yes' or 'No'")


if __name__ == "__main__":
    main()
