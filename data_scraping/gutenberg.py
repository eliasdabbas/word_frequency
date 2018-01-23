import requests
from bs2 import BeautifulSoup
import pandas as pd


page = 'https://www.gutenberg.org/ebooks/search/?sort_order=downloads&start_index='

final_df = pd.DataFrame()

for i in range(1, 1000, 25):
    temppage =  page + str(i)
    resp = requests.get(temppage)
    soup = BeautifulSoup(resp.text, 'lxml')
    titles = [x.text for x in  soup.select('.booklink .title')]
    downloads = [int(x.text.replace(' downloads', '')) for x in soup.select('.extra')]
    temp_df = pd.DataFrame({
        'title': titles,
        'downloads': downloads,

    })
    final_df = final_df.append(temp_df).reset_index(drop=True)
