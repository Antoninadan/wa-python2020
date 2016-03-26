filename = 'data/example6.txt'

with open(filename, 'r') as file:
    lines = file.readlines()

lines = filter(lambda line: 'delete me' not in line, lines)

with open(filename, 'w') as file:
    file.writelines(lines)
