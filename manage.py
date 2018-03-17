import json, csv, os, requests, datetime

class Manage(object):

    def __init__(self):
        pass

    def checkWallet(name):
        if os.path.isfile(name) == False:
            print("NO WALLET FOUND!\nCreate new account!")
            account = input('What is your name?: ')
            money = input('How much money to invest?: ')
            with open(name, 'w') as csvfile:
                t = datetime.datetime.now().strftime('%H:%M:%S')
                filewriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(['time', t])
                filewriter.writerow(['id', 1])
                filewriter.writerow(['name', account])
                filewriter.writerow(['BTH', money])
                filewriter.writerow(['BTC', 0])
            exit()
        else:
            print("WALLET FOUNDED!")
            print('-----------------------------')
            with open(name) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    print(row)
                return(reader)
    def getData(url):
        r = requests.get(url)
        r = r.json()
        return r
