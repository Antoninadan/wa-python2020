print('before exception')

try:
    print('before exception inside try')
    raise ValueError('supplied value is incorrect')
    print('after exception inside try')
except ValueError:
    print('exception caught')

print('after exception')
