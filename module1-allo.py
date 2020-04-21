import time
import requests
import json
from bs4 import BeautifulSoup as BS
#import codecs
from multiprocessing import Pool
import alphabet
from random import choice, uniform
import csv
import sqlite3


def write_csv(name, data):
    with open(name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        print(data)

def write_to_db(db_name, db_data):

    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    with connection:
        cursor.execute('''CREATE TABLE IF NOT EXISTS test_1 (object_id TEXT, hint TEXT)''')
        cursor.executemany('INSERT INTO test_1 VALUES (?,?)', db_data)

    connection.commit()

def get_hint(data):
    tt = uniform(0,2)
    time.sleep(tt)
    db_data = []
    txt = 'MISTAKE'
    headers = {'User-Agent': choice(alphabet.userag)}
    proxy = {'http': 'http://'+ choice(alphabet.proxies)}
    url = 'https://allo.ua/ua/catalogsearch/ajax/suggest/?currentTheme=main&currentLocale=uk_UA'
    try:
        r = requests.post(url, headers=headers, proxies=proxy, data=data)
        if r.status_code == 200:
            txt = r.text
            if r.text:
                d = (data['q'], str( json.loads(txt)["query"]))
                db_data.append(d)

            else:
                 obj = 'NO_DATA'
                 d = [data['q'], obj]
                 db_data.append(d)
                 write_csv('test_data', d)


        elif r.status_code == 429:
            time.sleep(2)
            get_hint(data)
            write_csv('mist2.csv', data['q'])

    except Exception as e:
        print(e,txt)

    connection = sqlite3.connect('test_1')
    cursor = connection.cursor()

    with connection:
        cursor.execute('''CREATE TABLE IF NOT EXISTS test_1 (object_id TEXT, hint TEXT)''')
        cursor.executemany('INSERT INTO test_1 VALUES (?,?)', db_data)

    connection.commit()
    return txt


def main():


    pool = Pool(processes=20)
    pool.map(get_hint,  [{'q':alphabet.list_input(2)[i], 'isAJax': 1} for i in range(len(alphabet.list_input(2)))])


if __name__ == '__main__':
    x = time.time()
    main()
    print(time.time() - x)

