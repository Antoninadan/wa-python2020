def perform_operation(operation, first, second):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    else:
        raise NotImplementedError('operation not supported')


def input_number(prompt):
    try:
        return float(input(prompt))
    except ValueError as error:
        print('Error:', error)
        return input_number(prompt)


while True:
    try:
        first_number = input_number('First number: ')
        operation = input('Operation: ')
        second_number = input_number('Second number: ')
        result = perform_operation(operation, first_number, second_number)
        print(result)
    except (ZeroDivisionError, NotImplementedError) as error:
        print('Error:', error)
    print()
