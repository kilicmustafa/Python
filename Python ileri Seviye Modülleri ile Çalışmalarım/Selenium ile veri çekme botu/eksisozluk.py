from selenium import webdriver

import time 
import random 

browser = webdriver.Firefox()


url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="


sayac = 1 


texts = list()

while sayac <= 10:
    number = random.randint(1,1927)
    newUrl = url + str(number)

    browser.get(newUrl)

    
    articles = browser.find_elements_by_css_selector(".content")


    for article in articles :
        
        texts.append(article.text)
        

    time.sleep(3)

browser.close()

m_sırası = 1

with open("entries.txt" , "w" ,encoding="UTF-8") as file:
    for text in text:
        file.write(str(m_sırası) + ".\n*" + text +"\n")
        file.write("-------------------------------\n")
        m_sırası +=1



        

