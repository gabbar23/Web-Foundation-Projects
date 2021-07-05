from dotenv import dotenv_values
import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

config = dotenv_values(".env")
PROMISE_SPEED=60
PROMISE_DOWN_SPEED=60
CHROME_DRIVER="chromedriver"

TWITTER_EMAIL=config["EMAIL"]
TWITTER_PASSWORD=config["PASSWORD"]



class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=CHROME_DRIVER)
        self.up=0
        self.down=0
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        speed=self.driver.find_element_by_class_name("start-text")
        speed.click()
        time.sleep(60)
        self.up=(self.driver.find_element_by_class_name("download-speed")).text
        self.down=(self.driver.find_element_by_class_name("upload-speed")).text
        

    def tweet_at_provider(self):
        time.sleep(2)

        self.driver.get("https://twitter.com/home")
        time.sleep(3)
        username=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_EMAIL)
        password=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(1)
        password.send_keys(Keys.ENTER)
        time.sleep(1)
        form=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        form.send_keys(f"aye yo! why is my internet speed is {self.up} Upload  and {self.down} Download  while i was promissed {PROMISE_DOWN_SPEED} Download and {PROMISE_SPEED} Upload")



bot=InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()