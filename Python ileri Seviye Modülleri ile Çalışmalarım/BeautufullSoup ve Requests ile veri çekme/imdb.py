import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

html_icerik = response.content
soup = BeautifulSoup(html_icerik,"html.parser")
imdb = float(input("Rating ? "))

basliklar = soup.find_all("td", {"class" : "titleColumn"})
ratingler = soup.find_all("td" , {"class" : "ratingColumn imdbRating"})


for baslik , rating in zip(basliklar ,ratingler):
    baslik = baslik.text
    baslik = baslik.replace("\n" , "")
   
    

    rating = rating.text
    
    rating = rating.replace("\n" ," ")
    
    
    if (float(rating) > imdb):
        print("Film adı : {} Film rating : {}".format(baslik , rating))

    
    print("Film adı : {} Film rating : {}".format(baslik , rating))