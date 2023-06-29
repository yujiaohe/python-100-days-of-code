from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/heyujiang/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://www.python.org/")

# search_bar = driver.find_element(by=By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
# print(logo.size)
# print(By.CLASS_NAME)

# documentation_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
events = {}
for index in range(0, len(event_times)):
    events[index] = {
        'time': event_times[index].text,
        'name': event_names[index].text
    }

print(events)
# shutdown the entire browser
driver.quit()
# close particular tab
# driver.close()
