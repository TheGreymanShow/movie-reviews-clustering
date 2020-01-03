# Year of Release

import bs4 as BeautifulSoup
import urllib.request
import pandas as pd

movie="12 angry men"
movie=movie.replace(" ","+")

from urllib.request import Request, urlopen
req = Request("https://www.google.com/search?q="+ movie +"+movie+release+date&ie=utf-8&oe=utf-8&client=firefox-b-ab", headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup.BeautifulSoup(webpage,'lxml')

year=[]
for div in soup.find_all("div"):
    #print(div.text)
    text="Release date:"
    text2="Initial release:"
    if text in div.text or text2 in div.text:
       year.append(div.text)
    
year=year[2]
year=year.split(" ")
year=year[2:]
year=' '.join(year)
