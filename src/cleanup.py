import bs4 as BeautifulSoup
import urllib.request
import pandas as pd
from urllib.request import Request, urlopen

df = pd.read_csv("D:/Projects/Movie Reviews Clustering/clustering_dataset.csv")

for index,row in df.iterrows():
    year=row['Year']
    year=str(year).split(' ')
    mid=0
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    
    if len(year)>2:
        month=year[1]
        #year=year[2]
            
        if month in months:
            mid=months.index(month)+1
    
        df.loc[index,"Month"]=mid
        #df.loc[index,"Year_2"]=year
        
df.to_csv("D:/Projects/Movie Reviews Clustering/clustering_dataset.csv")