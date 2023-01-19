import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from config import TWITTER_USER_EMAIL, TWITTER_PASSWORD

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_URL = "https://www.twitter.com"
INTERNET_SPEED_URL = "https://www.speedtest.net/"
CHROME_DRIVER_PATH = "/Users/rafaelqueiroz/Desktop/chromedriver"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(INTERNET_SPEED_URL)
        time.sleep(15)
        speed_btn = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        speed_btn.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        if float(self.down) < PROMISED_DOWN or float(self.up) < PROMISED_UP:
            self.driver.get(TWITTER_URL)
            time.sleep(10)
            log_in_btn = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span')
            log_in_btn.click()
            time.sleep(15)
            email_input = self.driver.find_element(By.XPATH,
                                                   '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            email_input.send_keys(TWITTER_USER_EMAIL, Keys.ENTER)
            time.sleep(5)
            try:
                username_request = self.driver.find_element(By.XPATH,
                                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
                username_request.send_keys("DuWatcher", Keys.ENTER)
                time.sleep(5)
                password_input = self.driver.find_element(By.XPATH,
                                                          '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
                password_input.send_keys(TWITTER_PASSWORD, Keys.ENTER)
                time.sleep(10)
            except NoSuchElementException:
                password_input = self.driver.find_element(By.XPATH,
                                                          '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
                password_input.send_keys(TWITTER_PASSWORD, Keys.ENTER)
                time.sleep(10)

            send_tweet = self.driver.find_element(By.XPATH,
                                                  '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
            send_tweet.click()
            time.sleep(5)
            message = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            message.send_keys(
                f"Hey @dutweets, current internet speed. Download at {self.down} Mbps Upload at {self.up} Mbps. Way below what is in the contract. Please check it out. Tks")
            tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
            tweet.click()
            time.sleep(100)
        else:
            pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
