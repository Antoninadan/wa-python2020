import os

data_filename = 'data/example6.txt'
result_filename = 'tmp.txt'

with open(data_filename, 'r') as data, \
        open(result_filename, 'w') as result:
    for line in data:
        if 'delete me' not in line:
            result.write(line)

os.rename(result_filename, data_filename)
