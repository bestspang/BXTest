import json, csv, os, requests
import datetime, time
from manage import Manage as mng

kw = ['secondary_currency', 'last_price', 'change']
r = mng.getData('https://bx.in.th/api/')
BTC = r['1']
previous = float(BTC[kw[1]])

reader = mng.checkWallet('wallet.csv')
print('-----------------------------')
text = 'initialize'
for i in range(10):
    text = text + '.'
    print(text, end='\r')
    time.sleep(0.5)
while True:
    BTC = mng.getData('https://bx.in.th/api/')['1']
    #print('-----------------------------')
    t = datetime.datetime.now().strftime('%H:%M:%S')
    #for i in r.items():
        #print('time: {} | {} | last price : {:.2f} | change: {}%'.format(t, i[1][kw[0]], i[1][kw[1]], i[1][kw[2]]))
    print('-----------------------------')
    #print('time: {} | {} | last price : {:.2f} | change: {}%'.format(t, BTC[kw[0]], BTC[kw[1]], BTC[kw[2]]), end='\r')
    print('time: {} | {} | last price : {:.2f} | change: {}%'.format(t, BTC[kw[0]], BTC[kw[1]], BTC[kw[2]]))
    print('-----------------------------')
    if float(BTC[kw[1]]) > previous:
        print('price up!')
    elif float(BTC[kw[1]]) == previous:
        print('same!')
    else:
        print('price down!')
    previous = float(BTC[kw[1]])
    time.sleep(2)
