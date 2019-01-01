from bs4 import BeautifulSoup
import urllib.request as request
import re, csv, time
# from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
from urllib.error import *
import concurrent.futures

def parse_wallet(name):
    print(name)
    page = 1
    start_time = time.time()

    while True:
        try:
            with request.urlopen('https://www.walletexplorer.com/wallet/' + str(name) + '/addresses') as opened_url:
                soup = BeautifulSoup(opened_url.read(), 'html.parser')
                break
        except (HTTPError, URLError) as e:
            print('https://www.walletexplorer.com/wallet/' + str(name) + '/addresses?page=' + str(page) + ' Error: ' + str(e))
            time.sleep(1)
            continue

    paging = soup.find('div', 'paging')
    last_page_regex = re.compile('Page \d+ / (\d+)')
    last_page = int(last_page_regex.search(paging.text).group(1))

    with open(str(name) + '.csv', 'a', newline='') as csv_output:
        writer = csv.writer(csv_output)

        while page <= last_page:
            print('Wallet: ' + str(name) + ' Page: ' + str(page) + ' Time: ' + str(time.time() - start_time))
            if page > 1:
                try:
                    with request.urlopen('https://www.walletexplorer.com/wallet/' + str(name) + '/addresses?page=' + str(page)) as opened_url:
                        soup = BeautifulSoup(opened_url.read(), 'html.parser')
                except (HTTPError, URLError) as e:
                    print('Error: ' + str(e))
                    time.sleep(1)
                    continue
            table = soup.find('table')
            addresses = table.find_all('a')

            for address in addresses:
                writer.writerow([name, address.text])

            page += 1


with open('top_wallets_Scan_uniq', mode = 'r') as file:
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        for wallet_name in file:
            executor.submit(parse_wallet, wallet_name.split(' ')[0])
