import requests

from bs4 import BeautifulSoup

url = "https://www.yellowpages.com/search?search_terms=ankara&geo_location_terms=Turkey+City%2C+PA"
response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi , "html.parser")

"""for i in soup.find_all("a"):
    print(i.get("href"))
    print(i.text)
    print("*********************")
"""



for i in soup.find_all("div" ,{"v-card"}):
    print(i)
    print("*****************************")