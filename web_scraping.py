#importing

from selenium.webdriver import Chrome
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

#url
imdb_url = 'https://www.imdb.com/'

url = 'https://www.imdb.com/chart/top/'

# headers=({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

# web = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)','Accept-Language': 'US-en'
# },).text

# soup = BeautifulSoup(web, 'html.parser' )

driver = Chrome()
driver.get(url)
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')
# driver.close()

movies = soup.find('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-2b8fdbce-0 emPbxy compact-list-view ipc-metadata-list--base")

tab = movies.find_all('li', class_="ipc-metadata-list-summary-item")


data=[]

for i in range(len(tab)):
    href = tab[i].a['href']
    url = imdb_url + href
    web = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Accept-Language': 'US-en'
    }).text

    soup = BeautifulSoup(web, 'html.parser' )
    print(type(soup))
    title = soup.find('div', class_="sc-13687a64-0 iOkLEK").find('span', class_="hero__primary-text").text.strip()

    year = soup.find('ul', class_="ipc-inline-list ipc-inline-list--show-dividers sc-cb6a22b2-2 aFhKV baseAlt baseAlt").li.text

    imdb_rating = soup.find('div', class_='sc-de99a7b2-3 bYeGeo').find('span', class_='sc-4dc495c1-1 lbQcRY').text

    rating = soup.find('ul', class_="ipc-inline-list ipc-inline-list--show-dividers sc-cb6a22b2-2 aFhKV baseAlt baseAlt").li.next_sibling
    rating = rating.a.text if rating.a else None

    runtime = soup.find(string='Runtime').next_element.text

    director = soup.find(string=['Director','Directors']).next_element
    director = [d.text for d in director]

    box_office = soup.find(string='Gross worldwide')
    box_office = box_office.next_element.text if box_office else None

    cast = soup.find('div', class_="ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l ipc-shoveler__grid").find_all('a', class_='sc-10bde568-1 jBmamV')[:3]
    casts=[c.text for c in cast]

    genre = soup.find('div', class_='ipc-chip-list__scroller').find_all('span')
    genres = [g.text for g in genre]

    votes = soup.find('div', class_='sc-9d3bc82f-3 kZxGGs').find('div', class_='sc-4dc495c1-3 eNfgcR').text

    data.append([title,year,imdb_rating,votes, genres,director, casts, box_office, runtime])

    df=pd.DataFrame(data, columns=['Title','Year','Imdb_rating','Votes','Genres','Director','Casts','Box_office','Runtime'])
    df.to_csv('imdb_test.csv', index=False)
