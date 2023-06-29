import json
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

PROMISED_DOWN = 500
PROMISED_UP = 50
CHROME_DRIVER_PATH = "your chromedriver path"


class InternetSpeedBot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.up = 0
        self.down = 0
        self.get_internet_speed()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        go = self.driver.find_element(by=By.CLASS_NAME, value="start-text")
        go.click()
        time.sleep(60)
        speed = self.driver.find_elements(by=By.CLASS_NAME, value="result-data-large")
        self.down = float(speed[0].text)
        self.up = float(speed[1].text)
        self.driver.quit()

    def sina_at_provider(self):
        self.driver.get("https://weibo.com/login.php")
        with open("sina_cookies.txt", "r", encoding='utf-8') as file:
            cookies = json.loads(file.read())
        time.sleep(5)
        for cookie in cookies:
            cookie_dict = {
                "domain": ".weibo.com",
                "name": cookie.get("name"),
                "value": cookie.get("value"),
                "expires": "",
                "path": "/",
                "httpOnly": False,
                "HostOnly": False,
                'Secure': False
            }
            self.driver.add_cookie(cookie_dict)
        time.sleep(3)
        self.driver.refresh()
        time.sleep(10)
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            text = self.driver.find_element(by=By.CLASS_NAME, value="Form_input_2gtXx")
            text.send_keys(f"[Python Internet Speed Bot]Hey Internet Provider, why is my internet speed "
                           f"{self.down}down/{self.up}up "
                           f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
            send_button = self.driver.find_element(by=By.XPATH, value='//*[@id="homeWrap"]/div[1]/div/div[4]/div/div[4]/button')
            send_button.click()
            print("发微博了")

    def get_cookies(self):
        self.driver.get("https://weibo.com/login.php")
        time.sleep(30)
        cookies = self.driver.get_cookies()
        json_cookies = json.dumps(cookies)

        with open("sina_cookies.txt", "w") as file:
            file.write(json_cookies)
        print("cookies saved!")