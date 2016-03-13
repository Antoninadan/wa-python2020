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


while True:
    try:
        first_number = float(input('First number: '))
        operation = input('Operation: ')
        second_number = float(input('Second number: '))
        result = perform_operation(operation, first_number, second_number)
        print(result)
    except (ZeroDivisionError, ValueError, NotImplementedError) as error:
        print('Error:', error)
    print()
