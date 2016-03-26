import datetime

now = datetime.datetime.now()

with open('data/log.txt', 'a') as log:
    print('Current date and time:', now, file=log)
