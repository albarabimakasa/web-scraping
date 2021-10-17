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

soup.header

soup.div

soup.h1

soup.header.p

