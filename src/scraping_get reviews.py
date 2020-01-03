import bs4 as BeautifulSoup
import urllib.request
import pandas as pd

df = pd.read_csv("D:/Projects/Movie Reviews Clustering/reviews.csv")

for index,row in df.iterrows():
    print(row['Movies'])
    url=row["URL"]
    src = urllib.request.urlopen("https://wogma.com/"+url)
    soup = BeautifulSoup.BeautifulSoup(src,'lxml')
    
    '''
    # Quick Review       
    div=soup.find("div",class_="coloring")
    quick_review=""
    for p in div.find_all("p"):
        quick_review=quick_review + p.text
    
    df.loc[index,'Quick Review'] = quick_review
    
    # Full Review
    div=soup.find("div",class_="tab-pane active")
    full_review=""
    for p in div.find_all("p"):
        full_review=full_review+p.text
    
    
    df.loc[index,'Full Review'] = full_review
    
    '''
    '''
    # Movie Details and Tags
    x,y,temp=[[],[],[]]
    #key
    for div in soup.find_all("div",class_="col-xs-12 col-sm-4 col-md-3"):
        for div in div.find_all("div"):
            text=div.text
            text=text[:-1]
            x.append(text)
    #value
    for div in soup.find_all("div",class_="col-xs-12 col-sm-8 col-md-9"):
        for a in div.find_all("a"):
            temp.append(a.text)
        temp=','.join(temp)
        y.append(temp)
        temp=[]
        
    details=["Official Sites","Banner","Producer","Director","Lead Cast","Supporting Cast","Story","Screenplay","Dialogues","Cinematography","Editor","Background Score","Action Choreography","Music Director","Lyrics","Costume Designer","Running time","Reviewer","Language","Country","Genres"]
        
    for parameter in x:
        pos=x.index(parameter)
        if parameter in details:
            df.loc[index,parameter] = y[pos]
    
         
    # Reader Reviews
    src = urllib.request.urlopen("https://wogma.com/movie/"+movie+"-urating/")
    soup = BeautifulSoup.BeautifulSoup(src,'lxml')
    
    reader_reviews=[]
    div=soup.find("div",class_="urating_list")
    for p in div.find_all("p"):
        review=p.text.strip()
        review=review.split(",")
        review[1]=review[1].replace("\n","")
        review[1]=review[1].lstrip()
        
        reader_reviews.append(review)'''
    
    
    
    # Year of Release    
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
    df.loc[index,"Year"] = year
    
    '''
    # Critic Reviews
    src = urllib.request.urlopen("https://wogma.com/movie/"+movie+"-/teho")
    soup = BeautifulSoup.BeautifulSoup(src,'lxml')
    
    # Twitter Reviews
    src = urllib.request.urlopen("https://wogma.com/movie/"+movie+"-wtwit/")
    soup = BeautifulSoup.BeautifulSoup(src,'lxml')
    
    '''
df.to_csv("D:/Projects/Movie Reviews Clustering/reviews.csv")