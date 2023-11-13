import random

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("ERROR: Invalid input. Please enter an integer.")
def perform_calculation(operator, a, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            print("ERROR: Division by zero. Changing the right-hand term to 1.")
            b = 1
        return a / b
    elif operator == '//':
        if b == 0:
            print("ERROR: Floor division by zero. Changing the right-hand term to 1.")
            b = 1
        return a // b
    elif operator == '%':
        if b == 0:
            print("ERROR: Modulus by zero. Changing the right-hand term to 1.")
            b = 1
        return a % b
    elif operator == '**':
        return a ** b
    else:
        print("ERROR: Invalid operator. Please enter '+', '-', '*', '/', '//', '%', or '**'")
        return None


def luckyNumber(a, b):
    if a < b:
        return random.randint(a, b + 1)
    else:
        return random.randint(b, a + 1)

print("Lucky Calculator!\n")
print("What would you like to do?\n")
choice = input("[c]alculator, [l]ucky number, [q]uit: ")
print()

if choice == 'c':
   
    calculation = input("Please Choose a Calculation [+], [-], [*], [/], [//], [%], [**]: ")
    left_term = get_integer_input("Please Enter An Integer: ")
    right_term = get_integer_input("Please Enter An Integer: ")

    result = perform_calculation(calculation, left_term, right_term)
    if result is not None:
        print("The result of your calculation was:", result)
elif choice == 'l':
    
    left_term = get_integer_input("Please Enter An Integer: ")
    right_term = get_integer_input("Please Enter An Integer: ")

    lucky_num = luckyNumber(left_term, right_term)
    print("Your lucky number is:", lucky_num)
elif choice == 'q':
    
    print("Goodbye!")
else:
    print("ERROR: I did not understand your input... Please try again...")

