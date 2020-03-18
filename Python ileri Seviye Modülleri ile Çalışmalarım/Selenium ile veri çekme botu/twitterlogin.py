from selenium import webdriver
import time

browser = webdriver.Firefox()

url = "https://twitter.com/?lang=en"

browser.get(url)

time.sleep(3)
login = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/a[2]")




login.click()

username = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")

password = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")

username.send_keys("Kullanıcı adınız")
password.send_keys("Şifreniz")



time.sleep(3)


login_in = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[3]/div")

login_in.click()

time.sleep(3)

browser.close()



