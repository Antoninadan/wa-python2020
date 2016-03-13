try:
    print(2 / 0)
except ZeroDivisionError:
    print('division by zero')
except ArithmeticError:
    print('arithmetic error occured')

