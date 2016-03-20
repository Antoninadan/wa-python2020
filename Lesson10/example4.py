import asyncio
import random


async def consume():
    count = 0
    sum_ = 0
    mean = 0
    while True:
        value = await produce()
        count += 1
        sum_ += value
        mean = sum_ / count
        print('''
        Data:        {0}
        Count:       {1}
        Running sum: {2}
        Mean:        {3}
        '''.format(value, count, sum_, mean))


async def produce():
    await asyncio.sleep(1)
    return random.randint(0, 100)


async def hello_task():
    while True:
        print('Hello from a coroutine!')
        await asyncio.sleep(0.5)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = asyncio.wait([consume(), hello_task()])
    loop.run_until_complete(tasks)
