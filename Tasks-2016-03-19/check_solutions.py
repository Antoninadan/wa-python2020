import sys
import os.path

dirname = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirname)


def check_task1(module):
    assert list(module.my_range(5)) == [0, 1, 2, 3, 4]
    assert list(module.my_range(0)) == []


def check_task2(module):
    assert list(module.repeat_chars('Python', 2)) == \
           ['P', 'P', 'y', 'y', 't', 't', 'h', 'h', 'o', 'o', 'n', 'n']
    assert list(module.repeat_chars('abc', 1)) == ['a', 'b', 'c']
    assert list(module.repeat_chars('abc', 0)) == []
    assert list(module.repeat_chars('', 1)) == []


def check_task3(module):
    assert list(module.fibonacci(5)) == [1, 1, 2, 3, 5]
    assert list(module.fibonacci(0)) == []


def check(task_name):
    module_name = task_name
    function_name = 'check_' + task_name
    module = __import__(module_name)
    function = globals()[function_name]
    try:
        function(module)
    except Exception as error:
        print(error, file=sys.stderr)
        print('Solution of', task_name, 'is incorrect', file=sys.stderr)
        print(file=sys.stderr)
    else:
        print(task_name, 'is implemented correctly')
        print()


tasks = ['task1', 'task2', 'task3']
for task in tasks:
    check(task)
