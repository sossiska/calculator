def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

def main():
    print("Welcome to the calculator program!")
    print("Please select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1/2/3/4): ")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print("The sum of", num1, "and", num2, "is", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("The difference between", num1, "and", num2, "is", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("The product of", num1, "and", num2, "is", result)
    elif choice == '4':
        result = divide(num1, num2)
        print("The quotient of", num1, "and", num2, "is", result)
    else:
        print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
