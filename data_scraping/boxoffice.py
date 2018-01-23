import requests
from bs4 import BeautifulSoup

final_list = []
for i in range(1, 155):
    page = 'http://www.boxofficemojo.com/alltime/domestic.htm?page=' + str(i) + '&p=.htm'
    resp = requests.get(page)
    soup = BeautifulSoup(resp.text, 'lxml')
    table_data = [x.text for x in soup.select('tr td')[11:511]]  # trial and error to get the exact positions
    temp_list = [table_data[i:i+5] for i in range(0, len(table_data[:-4]), 5)] # put every 5 values in a row
    for temp in temp_list:
        final_list.append(temp)