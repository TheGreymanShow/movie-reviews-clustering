import bs4 as BeautifulSoup
import urllib.request
import pandas as pd

src = urllib.request.urlopen("https://wogma.com/movies/alphabetic/basic/")
soup = BeautifulSoup.BeautifulSoup(src,'lxml')

table = soup.find('table')
table_rows = table.find_all('tr')

ls=[]
row=[]
count=0
link=""

for tr in table_rows:
    #getting the Movie name, Verdict, Rating
    row=[]
    td = tr.find_all('td')
    for i in td:
        text=i.text.strip()
        text=text.replace("\n","")
        text=text.replace("\r","")
        text=text.split(" ")
        
        #getting the URL
        r=text.count("")
        for j in range(r):
            text.remove("")
        text=' '.join(text)
        row.append(text)    
        
    urls=tr.find_all('a')
    for j in urls:
        x=j.get('href')
        if 'review' in x:
            link=x
    
    row.append(link)
    ls.append(row)
    
df=pd.DataFrame(ls,columns=['Movies','Verdict','Ratings','URL'])
df.to_csv("D:/Projects/Movie Reviews Clustering/new_reviews.csv")