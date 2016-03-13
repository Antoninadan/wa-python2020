print('before exception')

try:
    raise ValueError('supplied value is incorrect')
except ValueError:
    print('exception caught')

print('after exception')
