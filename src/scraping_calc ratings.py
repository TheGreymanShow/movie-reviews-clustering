import numpy as np
import pandas as pd

df = pd.read_csv("D:/Projects/Movie Reviews Clustering/new_reviews.csv")
avg,critic_value,reader_value,tweet_value=[0, 0, 0, 0]

for index, row in df.iterrows():
     temp=str(row['Dummy'])
     temp=temp.split(' ')
     
     
     if 'Critic' in temp:
         pos = temp.index('Critic') + 2
         critic_rating=temp[pos] 
         df.loc[index,'Critic Ratings'] = critic_rating
         if len(critic_rating)==5:
             critic_value= float(critic_rating[0])
         else:
             critic_value= float(critic_rating[:3])
     else:
         df.loc[index,'Critic Ratings'] = "NA"
         
     if 'Reader' in temp:
         pos = temp.index('Reader') + 2
         reader_rating=temp[pos] 
         df.loc[index,'Reader Ratings'] = reader_rating
         if len(reader_rating)==5:
             reader_value= float(reader_rating[0])
         else:
             reader_value= float(reader_rating[:3])
         
     else:
         df.loc[index,'Reader Ratings'] = "NA"
         
     if 'Tweet' in temp:
         pos = temp.index('Tweet') + 2
         tweet_rating=temp[pos] 
         df.loc[index,'Tweet Ratings'] = tweet_rating
         if len(tweet_rating)==5:
             tweet_value= float(tweet_rating[0])
         else:
             tweet_value= float(tweet_rating[:3])
         
     else:
         df.loc[index,'Tweet Ratings'] = "NA"
         
     values=[int(critic_value),int(reader_value),int(tweet_value)]
     zero_count=values.count(0)
     if zero_count==3:
         avg = "NA"
     elif zero_count==2:
         avg = critic_value + reader_value + tweet_value
     elif zero_count==1:
         avg = (critic_value + reader_value + tweet_value)/2
     else:    
         avg = (critic_value + reader_value + tweet_value)/3
     df.loc[index,'Avg Rating'] = avg
     
df.to_csv("D:/Projects/Movie Reviews Clustering/new_reviews.csv")