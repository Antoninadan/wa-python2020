import time
import random


def sleep(seconds):
    initial_time = time.time()
    while time.time() - initial_time < seconds:
        yield


def consume():
    count = 0
    sum_ = 0
    mean = 0
    while True:
        value = yield from produce()
        count += 1
        sum_ += value
        mean = sum_ / count
        print('''
        Data:        {0}
        Count:       {1}
        Running sum: {2}
        Mean:        {3}
        '''.format(value, count, sum_, mean))


def produce():
    yield from sleep(1)
    return random.randint(0, 100)


def hello_task():
    while True:
        print('Hello from a coroutine!')
        yield from sleep(0.5)


if __name__ == '__main__':
    consumer = consume()
    hello_printer = hello_task()
    while True:
        next(consumer)
        next(hello_printer)
        time.sleep(0.001)
