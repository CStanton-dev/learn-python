# Greeting
def welcome():
    print('Welcome to CStanton-dev\'s Calculator')

# A simple calculator
def calculate():

    instructions = 'Please type in the math operation you would like to complete:\n'
    instructions += '\t+ for addition\n'
    instructions += '\t- for subtraction\n'
    instructions += '\t* for multiplication\n'
    instructions += '\t/ for division\n'
    instructions += '-------------------------------------------------------------\n'
    operation = input(instructions)

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

    again()


# Funtion to ask the user if they want to run use the calculator again
def again():
    # User Input
    calc_again = input('Would you like to do something else? ')

    if calc_again.upper() == 'Y':
        calculate()

    elif calc_again.upper() == 'N':
        print('Exiting...')
        exit()

    else:
        print('Please provide a valid input...')
        again()

welcome()
calculate()
