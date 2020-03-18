from selenium import webdriver
import time


browser = webdriver.Firefox()


login_url = "https://twitter.com/"

browser.get(login_url)

time.sleep(3)

login_button = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/a[2]")

login_button.click()

username = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")

password = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")

login_in = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[3]/div")

username.send_keys("kullanıcı adı") #doldur
password.send_keys("passsword") #doldur

time.sleep(3)

login_in.click()


time.sleep(5)



search = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")

search.send_keys("aranacak kelime")#doldur

search.submit()


time.sleep(5)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)

tweets = browser.find_elements_by_css_selector(".css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0")


tweets_list = list()

for tweet in tweets :
    tweets_list.append(tweet.text)


with open("tweets.txt" ,"w" ,encoding="UTF-8") as file:

    for tweet in tweets_list:
        file.write(tweet+"\n")


browser.close()






