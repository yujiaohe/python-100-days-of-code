import os
import smtplib
import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Schwinn-Discover-Featuring-Aluminum-Drivetrain/dp/B0030U8SU6/ref=sr_1_4?keywords=bicyle&qid=1679047669&sr=8-4&th=1"
PRICE_LIMIT = 550

headers = {
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/111.0.0.0 Safari/537.36"
}
response = requests.get(URL, headers=headers)
print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())
price_html = soup.find(name="span", class_="a-size-mini olpMessageWrapper")
price = float(price_html.getText().strip().split("$")[1])
product_title = soup.find(name="span", id="productTitle").getText().strip()

email = os.getenv("GMAIL")
password = os.getenv("GMAIL_PASSWORD")

if price < PRICE_LIMIT:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        return_msg = connection.sendmail(from_addr=email,
                                         to_addrs=email,
                                         msg=f"Subject: Amazon Price Alert!\n\n{product_title} is now ${price}.\n{URL}"
                                         )
        print(return_msg)
        print("Email alert!")
