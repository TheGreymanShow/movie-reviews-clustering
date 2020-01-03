import bs4 as BeautifulSoup
import urllib.request
import pandas as pd

movie="12 angry men"
movie=movie.replace(" ","-")

src = urllib.request.urlopen("https://wogma.com/movie/"+movie+"-review/")
soup = BeautifulSoup.BeautifulSoup(src,'lxml')

# movie details as key-value pair
x,y,temp=[[],[],[]]
#key
for div in soup.find_all("div",class_="col-xs-12 col-sm-4 col-md-3"):
    for div in div.find_all("div"):
        x.append(div.text)
#value
for div in soup.find_all("div",class_="col-xs-12 col-sm-8 col-md-9"):
    for a in div.find_all("a"):
        temp.append(a.text)
    y.append(temp)
    temp=[]