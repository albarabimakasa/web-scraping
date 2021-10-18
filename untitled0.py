# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 06:21:03 2021

@author: Albara Bimakasa
"""

from bs4 import BeautifulSoup
import requests

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'

#request the web host to get url
page = requests.get(url)
page.text

#convert html to python using parser.lxml

soup = BeautifulSoup(page.text, 'lxml')
soup

#mengakses tag header
soup.header

#mengakses tag div
soup.div

#mengakses tag h1
soup.h1

#mengambil string dari tag dalam tag (nested tag)
soup.header.p
soup.header.p.string

#mengambil tag a dalam <header>
a_awal = soup.header.a
a_awal

#mendapatkan attributesnya saja
