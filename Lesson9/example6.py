def fibonacci():
    prev, last = 0, 1
    while True:
        yield last
        prev, last = last, prev + last


ten_fibs = list(zip(range(1, 11), fibonacci()))
print(ten_fibs)
