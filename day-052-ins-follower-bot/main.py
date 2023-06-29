import os
import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "/Users/heyujiang/Development/chromedriver"
SIMILAR_ACCOUNT = "shiba_watercolor"
USERNAME = os.getenv("INS_USERNAME")
PASSWORD = os.getenv("INS_PASSWORD")


class InstaFollower:

    def __init__(self):
        chrome_service = Service(executable_path=CHROME_DRIVER_PATH)
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.followers = 0

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)
        user_password = self.driver.find_elements(by=By.CLASS_NAME, value="_aa4b")
        user_password[0].send_keys(USERNAME)
        user_password[1].send_keys(PASSWORD)
        user_password[1].send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(3)
        follow_number = self.driver.find_elements(by=By.CLASS_NAME, value="_ac2a")
        self.followers = int(follow_number[2].text)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/following")
        time.sleep(5)
        scrolldown_button = self.driver.find_element(By.CSS_SELECTOR, 'button._acan._acap._acas')
        scrolldown_button.send_keys(Keys.PAGE_DOWN)

    def follow(self):
        for i in range(1, self.followers + 1):
            xpath = f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]' \
                    f'/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button'
            follow_button = self.driver.find_element(by=By.XPATH, value=xpath)
            try:
                follow_button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                stop_following = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]'
                                                                             '/div/div[2]/div[1]/div/div[2]'
                                                                             '/div/div/div/div/div/div/button[1]')
                stop_following.click()


if __name__ == "__main__":
    ins_follower = InstaFollower()
    ins_follower.login()
    ins_follower.find_followers()
    ins_follower.follow()