# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:40:10 2021

@author: Albara bimakasa
"""

import requests 
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/' 
page = requests.get(url)
page

soup = BeautifulSoup(page.text,'lxml')
soup

tabel = soup.find('table', id = 'main_table_countries_today')
tabel

headers = []

for i in tabel.find_all('th'):
    judul = i.text
    headers.append(judul)
    
headers[13] = 'Tests/1M pop'

dataku = pd.DataFrame(columns=(headers))

for j in tabel.find_all('tr')[1:]:
    data_baris = j.find_all('td')
    baris = [tr.text for tr in data_baris]
    panjang = len(dataku)
    dataku.loc[panjang] = baris
    
dataku.drop(dataku.index[0:7], inplace = True)
dataku.copy()
dataku.drop(dataku.index[224:230], inplace = True)
dataku.drop(dataku.index[224], inplace = True)
dataku.reset_index(inplace=True , drop = True)
dataku.drop('#', inplace = True, axis=1)

dataku.to_csv('data_covid.csv',index = False)