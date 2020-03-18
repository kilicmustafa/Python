from selenium import webdriver
import time

browser = webdriver.Firefox()


url = "https://www.instagram.com/"

browser.get(url)
time.sleep(3)




username = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
password = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
login_button = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]/button")



username.send_keys("kilicmustafa.tr")
password.send_keys("000000")
login_button.click()



skip = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
skip.click()

time.sleep(6)

profile_button = browser.find_element_by_css_selector(".aOOlW.HoLwm")
profile_button.click()





time.sleep(6)




browser.close()

