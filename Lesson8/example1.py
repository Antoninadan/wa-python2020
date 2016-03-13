print('before exception')

try:
    print('before exception inside try')
    var = 4 / 0
    print('after exception inside try')
except ZeroDivisionError:
    print('exception caught')

print('after exception')
