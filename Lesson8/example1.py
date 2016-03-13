print('before exception')

try:
    print('before exception inside try')
    choice = input('Выберите класс исключения: ')
    if choice == 'ValueError':
        raise ValueError('incorrect value')
    elif choice == 'ZeroDivisionError':
        2 / 0
    else:
        raise NotImplementedError(choice)
    print('after exception inside try')
except (ZeroDivisionError, ValueError) as error:
    print('exception caught:', error)

print('after exception')
