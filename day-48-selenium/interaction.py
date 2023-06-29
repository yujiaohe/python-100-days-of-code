from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "/Users/heyujiang/Development/chromedriver"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
# article_count.click()

community_portal = driver.find_element(by=By.LINK_TEXT, value="Community portal")
# community_portal.click()

search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


# driver.close()
