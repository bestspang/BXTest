#from urllib.request import urlopen as uReq
#from bs4 import BeautifulSoup as soup
import json
import requests
#import sys
import datetime

kw = ['secondary_currency', 'last_price', 'change']
url = "https://bx.in.th/api/"
r = requests.get(url)
r = r.json()
#print(type(r))
#print(r['1'])
#print(r['1']['last_price'])

for i in r.items():
    #enumerate(r[i].items())
    #print(/r'last price: {} : {:.2f}'.format(i[1]['secondary_currency'], i[1]['last_price']), end='/r')
    t = datetime.datetime.now().strftime('%H:%M:%S')
    #print('last price: {:.2f} {}'.format(i[1][kw[1]], i[1][kw[0]]))
    print('time: {} | {} | last price : {:.2f} | change: {}%'.format(t, i[1][kw[0]], i[1][kw[1]], i[1][kw[2]]))
    #sys.stdout.write('last price: {} : {:.2f} \r'.format(i[1]['secondary_currency'], i[1]['last_price']))
    #sys.stdout.flush()
#for k, v in r.items():



#data = json.loads(r)
#print(data)
#import urllib, json
#url = "http://maps.googleapis.com/maps/api/geocode/json?address=google"
#response = urllib.urlopen(url)
#data = json.loads(response.read())
#print data
