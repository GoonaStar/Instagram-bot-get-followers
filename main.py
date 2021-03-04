from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
SIMILAR_ACCOUNT = "_codehub_"
USERNAME = "Goona_9"
PASSWORD = os.environ.get("EMAIL_PASSWORD")

class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def find_xpath_element(self, xpath):
        is_found = False
        element = None
        while not is_found:
            try:
                element = self.driver.find_element_by_xpath(xpath)
                time.sleep(3)
            except NoSuchElementException:
                is_found = False
            return element

    def login(self):
        self.driver.get(f"https://www.instagram.com/")
        time.sleep(3)
        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        time.sleep(2)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(3)
        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        login.click()

        time.sleep(3)
        # base_window = self.driver.window_handles[0]
        # pop_up_window = self.driver.window_handles[1]
        # self.driver.switch_to.window(pop_up_window)
        # time.sleep(3)

        turn_off_button = self.find_xpath_element('/html/body/div[4]/div/div/div/div[3]/button[2]')
        turn_off_button.click()

        # self.driver.switch_to.window(base_window)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(4)
        followings = self.find_xpath_element('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followings.click()

        time.sleep(2)

        for i in range(10):
            self.find_xpath_element('/html/body/div[5]/div/div/div[2]//a').send_keys(Keys.END)
            time.sleep(4)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        try:
            for button in all_buttons:
                button.click()
                time.sleep(1)
            pass
        except ElementClickInterceptedException:
            cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
            cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()




