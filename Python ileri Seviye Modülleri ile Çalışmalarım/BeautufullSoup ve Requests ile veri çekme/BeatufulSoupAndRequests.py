from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.sinanerdinc.com/python").text

soup = BeautifulSoup(source , 'lxml')


heading = soup.find('div' ,class_="page-heading")

text = heading.h1.text
print(text)


ImgUrl = soup.find("img" ,class_="avatar-img")['src']

print(ImgUrl)


ImgSpl = ImgUrl.split("/")

print(ImgSpl)

ImgName = ImgSpl[2]
print(ImgName)


for post in soup.findAll("article" ,class_="post-preview"):


    try:
        postText = post.find("div" ,class_="post-entry").text
        #eger bu link olsaydı link olmadığı zaman hata vermesin diye yaptık..
    except Exception as e :


        pastText = None
    print(postText)