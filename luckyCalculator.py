import random


def getInput():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1, num2

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("Error: Division by zero. Setting divisor to 1.")
        num2 = 1
    return num1 / num2

def floor_divide(num1, num2):
    if num2 == 0:
        print("Error: Division by zero. Setting divisor to 1.")
        num2 = 1
    return num1 // num2

def modulus(num1, num2):
    if num2 == 0:
        print("Error: Division by zero. Setting divisor to 1.")
        num2 = 1
    return num1 % num2

def exponentiate(num1, num2):
    return num1 ** num2

def luckyNumber(low, high):
    return random.randint(low, high)


print("Lucky Calculator!")
print("By: <Tirtho Roy>")
print("[COM S 127 <section>]")
print()

while True:
    print("What would you like to do?")
    print("[c]alculator, [l]ucky number, or [q]uit")
    choice = input().lower()

    if choice == 'c':
        operation = input("Enter operation (+, -, *, /, //, %, **): ")
        if operation not in ['+', '-', '*', '/', '//', '%', '**']:
            print("Invalid operation!")
            continue

        num1, num2 = getInput()
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        elif operation == '//':
            result = floor_divide(num1, num2)
        elif operation == '%':
            result = modulus(num1, num2)
        elif operation == '**':
            result = exponentiate(num1, num2)

        print("Result:", result)

    elif choice == 'l':
        low = int(input("Enter the lower bound: "))
        high = int(input("Enter the upper bound: "))
        print("Your lucky number is:", luckyNumber(low, high))

    elif choice == 'q':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 'c', 'l', or 'q'.")

