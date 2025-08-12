def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Basic Mathematical Operations")
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    try:
        division = num1 / num2
    except ZeroDivisionError:
        division = "undefined (cannot divide by zero)"

    print(f"\nResults:")
    print(f"Addition: {num1} + {num2} = {addition}")
    print(f"Subtraction: {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division: {num1} / {num2} = {division}")

if __name__ == "__main__":
    main()
