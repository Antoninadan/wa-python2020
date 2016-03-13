try:
    raise Exception('some error')
except Exception:
    print('exception handled')
finally:
    print('this block is always executed')
