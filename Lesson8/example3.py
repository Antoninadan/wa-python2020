operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}


def input_number(prompt):
    try:
        return float(input(prompt))
    except ValueError as error:
        print('Error:', error)
        return input_number(prompt)


def input_operation(prompt):
    operation = input(prompt)
    try:
        return operations[operation]
    except KeyError:
        print('Unsupported operation:', operation)
        return input_operation(prompt)


while True:
    try:
        first_number = input_number('First number: ')
        operation = input_operation('Operation: ')
        second_number = input_number('Second number: ')
        result = operation(first_number, second_number)
        print(result)
    except ZeroDivisionError as error:
        print('Error:', error)
    print()
