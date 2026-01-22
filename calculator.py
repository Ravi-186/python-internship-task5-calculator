"""
Modular Calculator Program
Author: Ravi Tej
"""

def add(a, b):
    """Returns the sum of two numbers"""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers"""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers"""
    return a * b


def divide(a, b=1):
    """
    Returns the division of two numbers
    Handles division by zero
    """
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


def calculator_menu():
    """Displays calculator menu"""
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def main():
    """Main function to run calculator"""
    while True:
        calculator_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting calculator... Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == '1':
            print("Result:", add(num1, num2))

        elif choice == '2':
            print("Result:", subtract(num1, num2))

        elif choice == '3':
            print("Result:", multiply(num1, num2))

        elif choice == '4':
            print("Result:", divide(num1, num2))


if __name__ == "__main__":
    main()
