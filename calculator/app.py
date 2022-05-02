# A simple calculator
def calculate():
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    -------------------------------------------------------------
    ''')

    # User Input
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    # Addition
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    # Subtraction
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    # Multiplication
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    # Division
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    # No Input
    else:
        print('You have not typed a valid operator, please run the program again.')


calculate()
