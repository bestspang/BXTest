import csv, datetime
from manage import Manage as mng

# reader = mng.getData('https://bx.in.th/api/')['1']
# print(reader)

BTC = mng.getData('https://bx.in.th/api/')['1']
lastPrice = float(BTC['last_price'])


with open('wallet.csv') as csvfile:
    reader = list(csv.reader(csvfile))

    print('youy credits: {:,} {}'.format(float(reader[3][1]),reader[3][0]))
    buy = input('how much BTC you want to but?: ')
    print('connecting...')
    if float(buy) <= float(reader[3][1]):
        t = datetime.datetime.now().strftime('%H:%M:%S')
        reader[3][1] = float(reader[3][1]) - float(buy)
        reader[4][1] = float(buy) / lastPrice
        reader[0][1] = t
        print('your credits: {:,} {}'.format(float(reader[3][1]), reader[3][0]))
        print('you are received: {:,} {}'.format(float(reader[4][1]), reader[4][0]))
    else:
        print('not enough credit or wrong input!')

    print(reader)
