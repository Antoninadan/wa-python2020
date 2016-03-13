try:
    print(2 / 0)
except ArithmeticError:
    print('arithmetic error occured')
except ZeroDivisionError:
    print('division by zero')

