import os

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

FB_EMAIL = os.getenv("FB_EMAIL")
FB_PASSWORD = os.getenv("FB_PASSWORD")

chrome_driver_path = "/Users/heyujiang/Development/chromedriver"
chrome_service = Service(executable_path=chrome_driver_path)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://tinder.com/")

sleep(2)
login = driver.find_element(by=By.XPATH, value='//*[@id="q-586956664"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()

sleep(2)
facebook = driver.find_element(by=By.XPATH, value='//*[@id="q1979629556"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div')
facebook.click()

sleep(5)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(by=By.ID, value="email")
email.send_keys(FB_EMAIL)
password = driver.find_element(by=By.ID, value="pass")
password.send_keys(FB_PASSWORD)
# password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)
allow_location_button = driver.find_element(by=By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element(by=By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()


for n in range(100):
    sleep(2)
    try:
        like_button = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(by=By.CSS_SELECTOR, value=".itsMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()



