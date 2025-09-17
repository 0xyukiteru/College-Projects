"""Simple program to divide two numbers entered by the user."""


def get_number(prompt: str) -> float:
    """Prompt the user for a number and return it as a float."""
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Please enter a valid number.")


def divide_numbers(numerator: float, denominator: float) -> float:
    """Return the quotient of two numbers, raising an error if denominator is zero."""
    if denominator == 0:
        raise ValueError("Cannot divide by zero.")
    return numerator / denominator


def main() -> None:
    """Run the interactive division program."""
    print("Divide Two Numbers")
    numerator = get_number("Enter the numerator: ")

    while True:
        denominator = get_number("Enter the denominator: ")
        if denominator == 0:
            print("The denominator cannot be zero. Please try again.")
        else:
            break

    result = divide_numbers(numerator, denominator)
    print(f"{numerator} ÷ {denominator} = {result}")


if __name__ == "__main__":
    main()
