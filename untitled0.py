# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 06:21:03 2021

@author: Albara Bimakasa
"""
#import the library 

from bs4 import BeautifulSoup
import requests
import re

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'

#request the web host to get url
page = requests.get(url)
page.text

#convert html to python using parser.lxml

soup = BeautifulSoup(page.text, 'lxml')
soup

#how to access tag header
soup.header

#access tag div
soup.div

#access tag h1
soup.h1

#get string from tag in tag (nested tag)
soup.header.p
soup.header.p.string

#get tag a in <header>
a_awal = soup.header.a
a_awal

#get the attributes only
a_awal.attrs
a_awal['data-target']
a_awal['data-baru'] = 'ini adalah yang baru lo'
a_awal.attrs
a_awal
 
soup.header.div
 
#get specific attribute in a tag
 
soup.find('div',{'class':'side-collapse in'}) 
soup.find('div',{'class':'container-fluid blog-hero'})
soup.find('div',{'id':'layout-footer'}) 
 
soup.find('div', class_ ='container')
 
#use find all
soup.find_all('h4', class_ = 'pull-right price')
 
#slicing in find all
soup.find_all('h4', class_ = 'pull-right price')[2:5]
 
#get the data
 
nama = soup.find_all('a', class_ = 'title')
nama

deskripsi = soup.find_all('p', class_ = 'description')
deskripsi

harga = soup.find_all('h4', class_ = 'pull-right price')
harga

review = soup.find_all('p', class_ = 'pull-right')
review

rating = soup.find_all('div', class_ = 'ratings')
rating

bintang = soup.find_all('div',{'p':'data-rating'})
bintang


#make string from list find all 

nama_produk_list = []

for i in nama:
    name = i.text
    nama_produk_list.append(name)
    
    
harga_list = []

for i in harga:
    price = i.text
    harga_list.append(price)
        
    
deskripsi_list = []

for i in deskripsi:
    description = i.text
    deskripsi_list.append(description)
 

review_list = []

for i in review:
    reviewi = i.text
    review_list.append(reviewi)
 

bintang_list = []


html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

for tag in soup.find_all("div", {"class":"ratings"}):
    # get all child from the tags
    for h in tag.children:
        # convert to string data type
        s = h.encode('utf-8').decode("utf-8") 

        # find the tag with data-rating and get text after the keyword
        m = re.search('(?<=data-rating=)(.*)', s)
        
        # check if not None
        if m:
            #print the text after data-rating and remove last char
            bintang_list.append(m.group()[:-1])


import pandas as pd
tabel2 = pd.DataFrame({'nama produk': nama_produk_list,
                      'harga': harga_list,
                      'deskripsi produk': deskripsi_list,
                      'jumlah review':review_list,
                      'star': bintang_list })

