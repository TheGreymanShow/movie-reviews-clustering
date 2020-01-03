'''
import bs4 as BeautifulSoup
import urllib.request

src = urllib.request.urlopen("https://wogma.com/movies/alphabetic/basic/")
soup = BeautifulSoup.BeautifulSoup(src,'lxml')

table = soup.find('table')
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)
'''

import numpy as np
import pandas as pd

# part 1
#dfs = pd.read_html("https://wogma.com/movies/alphabetic/basic/")
#df=dfs[0]
#dfs[0].to_csv("D:/Projects/Movie Reviews Clustering/reviews.csv")

#part 2
df = pd.read_csv("D:/Projects/Movie Reviews Clustering/reviews.csv")
avg,critic_value,reader_value,tweet_value=[0,0,0,0]

for index, row in df.iterrows():
     temp=str(row['Dummy'])
     temp=temp.split(' ')
     if 'Critic' in temp:
         pos = temp.index('Critic') + 3
         critic_rating=temp[pos] 
         df.loc[index,'Critic Ratings'] = critic_rating
         if len(critic_rating)==5:
             critic_value= float(critic_rating[0])
         else:
             critic_value= float(critic_rating[:3])
     else:
         df.loc[index,'Critic Ratings'] = "NA"
         
     if 'Reader' in temp:
         pos = temp.index('Reader') + 3
         reader_rating=temp[pos] 
         df.loc[index,'Reader Ratings'] = reader_rating
         if len(reader_rating)==5:
             reader_value= float(reader_rating[0])
         else:
             reader_value= float(reader_rating[:3])
         
     else:
         df.loc[index,'Reader Ratings'] = "NA"
         
     if 'Tweet' in temp:
         pos = temp.index('Tweet') + 3
         tweet_rating=temp[pos] 
         df.loc[index,'Tweet Ratings'] = tweet_rating
         if len(tweet_rating)==5:
             tweet_value= float(tweet_rating[0])
         else:
             tweet_value= float(tweet_rating[:3])
         
     else:
         df.loc[index,'Tweet Ratings'] = "NA"
         
     avg = (critic_value + reader_value + tweet_value)/3
     df.loc[index,'Avg Rating'] = avg