try:
    raise Exception('some error')
finally:
    print('this block is always executed')
