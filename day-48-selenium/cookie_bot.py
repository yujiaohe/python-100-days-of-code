from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "/Users/heyujiang/Development/chromedriver"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.ID, value="cookie")

start_time = time.time()
five_seconds = start_time + 5
timeout = start_time + 60*1

while time.time() < timeout:
    cookie.click()
    if time.time() > five_seconds:
        money = driver.find_element(by=By.ID, value="money").text
        money = int(money.replace(",", ""))
        store = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        affordable_upgrades = {}
        for item in store[-2::-1]:
            upgrades = item.text.split("-")
            price = int(upgrades[1].strip().replace(",", ""))
            if money >= price:
                purchase_id = upgrades[0].strip()
                affordable_upgrades[purchase_id] = price
        if len(affordable_upgrades) > 0:
            purchase_id = max(affordable_upgrades, key=affordable_upgrades.get)
            print(purchase_id)
            purchase = driver.find_element(by=By.ID, value=f"buy{purchase_id}")
            purchase.click()
        five_seconds = time.time() + 5

cookies_second = driver.find_element(by=By.ID, value="cps")
print(cookies_second.text)
