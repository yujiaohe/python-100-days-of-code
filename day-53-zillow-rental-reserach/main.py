import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "/Users/heyujiang/Development/chromedriver"
GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfviI1XceZ8Zzb8lrsfhyMV6SXEIWlGuPlRdrCjW7LUHV1SaQ/viewform" \
              "?usp=sf_link"
ZILLOW = "https://www.zillow.com/homes/San-Francisco," \
         "-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA" \
         "%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south" \
         "%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId" \
         "%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A" \
         "%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D" \
         "%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value" \
         "%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22" \
         "%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D" \
         "%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"


class RentSearch:

    def __init__(self):
        chrome_service = Service(executable_path=CHROME_DRIVER_PATH)
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.rent_data = self.query_renting_list()

    def query_renting_list(self):
        headers = {
            'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36"
        }
        response = requests.get(ZILLOW, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        all_links = soup.find_all(name="a", class_="property-card-link")
        links = [f'https://www.zillow.com{item.get("href")}' if item.get("href")
                 else item.get("href") for item in all_links]
        links = list(dict.fromkeys(links))
        # print(len(links))
        all_addresses = soup.find_all(name="address", attrs={"data-test": "property-card-addr"})
        addresses = [item.getText().split(" | ")[-1] for item in all_addresses]
        # print(len(addresses))
        all_prices = soup.find_all(name="span", attrs={"data-test": "property-card-price"})
        prices = [item.getText().replace("/", "+").split("+")[0].strip() for item in all_prices]
        # print(len(prices))
        return [links, addresses, prices]

    def fill_form(self):
        for index in range(len(self.rent_data[0])):
            link = self.rent_data[0][index]
            address = self.rent_data[1][index]
            price = self.rent_data[2][index]
            self.driver.get(GOOGLE_FORM)
            time.sleep(3)
            inputs = self.driver.find_elements(by=By.CSS_SELECTOR, value=".Qr7Oae input")
            inputs[0].send_keys(address)
            inputs[1].send_keys(price)
            inputs[2].send_keys(link)
            submit_button = self.driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")
            submit_button.click()
            time.sleep(2)
            print(f"{address} with {price} added!")


if __name__ == "__main__":
    rs = RentSearch()
    rs.fill_form()

