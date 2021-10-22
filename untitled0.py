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
 a_awal.attrs
 a_awal['data-target']
 a_awal['data-baru'] = 'ini adalah yang baru lo'
 a_awal.attrs
 a_awal
 
 soup.header.div
 
 #mencari attribute tertentu dalam sebuah tag
 
 soup.find('div',{'class':'side-collapse in'}) 
 soup.find('div',{'class':'container-fluid blog-hero'})
 soup.find('div',{'id':'layout-footer'}) 
 
 soup.find('div', class_ ='container')
 
 #menggunakan find all
 soup.find_all('h4', class_ = 'pull-right price')
 
 #slicing pada find all
 soup.find_all('h4', class_ = 'pull-right price')[2:5]
 
 
 
nama = soup.find_all('a', class_ = 'title')
nama

deskripsi = soup.find_all('p', class_ = 'description')
deskripsi
 
review = soup.find_all('p', class_ = 'pull-right')
review

rating = soup.find_all('div', class_ = 'ratings')
rating
 
#membuat string dari list find all 

nama_produk_list = []

for i in nama:
    name = i.text
    nama_produk_list.append(name)
    
    
deskripsi_list = []

for i in deskripsi:
    description = i.text
    deskripsi_list.append(description)
 

rating_list = []

for i in rating:
    ratingsi = i.text
    rating_list.append(ratingsi)
 
soup.find('div',{'class':'side-collapse in'}) 
soup.find_all('div' ,{'p':'data-rating'}) 

 
 
 
 
 
 
 
 
 
 
 