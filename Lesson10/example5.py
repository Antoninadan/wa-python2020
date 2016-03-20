import asyncio
import functools
import select
import sys


def async_fibonacci(n, future):
    if n == 1 or n == 2:
        return future.set_result(1)

    prev_result = None

    def after_last_computation(last_future):
        future.set_result(prev_result + last_future.result())

    def after_prev_computation(prev_future):
        nonlocal prev_result
        prev_result = prev_future.result()
        last_future = asyncio.Future()
        asyncio.ensure_future(async_fibonacci(n - 2, last_future))
        last_future.add_done_callback(after_last_computation)

    prev_future = asyncio.Future()
    asyncio.ensure_future(async_fibonacci(n - 1, prev_future))
    prev_future.add_done_callback(after_prev_computation)

    yield


def async_input(prompt):
    # TODO: rewrite
    print(prompt, end='', flush=True)
    while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        yield
        line = sys.stdin.readline()
        if line:
            return line
    else:
        yield


def main():
    def callback(index, future):
        fib = future.result()
        print('F({}) = {}'.format(index, fib))

    while True:
        data = yield from async_input('Fibonacci index: ')
        n = int(data)
        future = asyncio.Future()
        asyncio.ensure_future(async_fibonacci(n, future))
        future.add_done_callback(functools.partial(callback, n))

        yield


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
