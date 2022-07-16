from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os

#CHROME BROWSER DRIVER DOWNLOAD LINK:-https://chromedriver.chromium.org/

chrome_driver_path = "ENTER HERE YOUR chromedriver.exe PATH OR OTHER BROWSER DRIVER PATH"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://twitter.com/login")
driver.fullscreen_window()

TWITTER_EMAIL="ENTER HERE YOUR TWITTER EMAIL"
TWITTER_PASSWORD="ENTER HERE YOUR TWITTER PASSWORD"
TWITTER_ID="ENTER HERE YOUR TWITTER ID"
sleep(5)

log_in = driver.find_element_by_name(name='text')
log_in.send_keys(TWITTER_EMAIL)
log_in.send_keys(Keys.ENTER)
sleep(5)
try:
    password = driver.find_element_by_name(name="password")
    password.send_keys(TWITTER_PASSWORD)
    password.send_keys(Keys.ENTER)
except NoSuchElementException:
    number=driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')        
    number.send_keys(TWITTER_ID)
    number.send_keys(Keys.ENTER)
    sleep(3)
    password = driver.find_element_by_name(name="password")
    password.send_keys(TWITTER_PASSWORD)
    password.send_keys(Keys.ENTER)

sleep(3)
Explore_Link = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]').click()

sleep(3)
search_twitter = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')
search_twitter.send_keys("#100DaysOfCode") #YOU CAN CHANGE/REPLACE #100DaysOfCode TO ANYOTHER SEARCH #KEYWORD.
search_twitter.send_keys(Keys.ENTER)

sleep(3)
latest_tweets=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[2]/a').click()

sleep(10)

for i in range(2):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(2) 

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+Keys.HOME)
sleep(3)
# likes=driver.find_elements_by_xpath("//div[@data-testid='like']")
likes=driver.find_elements(By.XPATH,"//div[@data-testid='like']")
for like in likes:
    like.click()
    sleep(3)

driver.quit()