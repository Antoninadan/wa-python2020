print('before exception')

try:
    print('before exception inside try')
    choice = input('Выберите класс исключения: ')
    if choice == 'ValueError':
        raise ValueError('incorrect value', 20, 10)
    elif choice == 'ZeroDivisionError':
        2 / 0
    else:
        raise NotImplementedError(choice)
    print('after exception inside try')
except ZeroDivisionError:
    print('intercepted division by zero')
except ValueError as error:
    print('intercepted value error')
    print('error message:', error.args)

print('after exception')
