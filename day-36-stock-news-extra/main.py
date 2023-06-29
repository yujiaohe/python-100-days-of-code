import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.environ["ENV_STOCK_API_KEY"]
NEWS_API_KEY = os.environ["ENV_NEWS_API_KEY"]

TWILIO_SID = os.environ["ENV_TWILIO_SID"]
TWILIO_AUTH_TOKEN = os.environ["ENV_TWILIO_TOKEN"]

FROM = os.environ["FROM"]
TO = os.environ["TO"]

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
  "function": "TIME_SERIES_DAILY_ADJUSTED",
  "symbol": STOCK,
  "apikey": STOCK_API_KEY,
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
prices_data = [value for _, value in stock_data.items()]
yesterday_close = float(prices_data[0]["4. close"])
before_yesterday_close = float(prices_data[1]["4. close"])
delta = (yesterday_close - before_yesterday_close) / yesterday_close
print(delta)

if abs(delta) > 0.01:
  print("Get News")

  ## STEP 2: Use https://newsapi.org
  # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
  news_params = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "searchIn": "title",
    "sortBy": "publishedAt",
  }
  response = requests.get(url=NEWS_ENDPOINT, params=news_params)
  response.raise_for_status()
  articles = response.json()["articles"]
  # print(articles)
  three_articles = articles[:3]
  # for article in three_articles:
  #     print(article["title"])
  #     print(html.unescape(article["description"]))
  #     print("===================")

  ## STEP 3: Use https://www.twilio.com
  # Send a seperate message with the percentage change and each article's title and description to your phone number.
  if delta > 0:
    header = f"🔺 {delta:.2%}"
  else:
    header = f"🔻 {-delta:.2%} "

  formatted_articles = [
    f"Headline: {article['title']}.\nBrief: {article['description']}."
    for article in three_articles
  ]
  client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
  for article in formatted_articles:
    message = client.messages.create(body=f"{STOCK}: {header}\n{article}",
                                     from_=FROM,
                                     to=TO)
    print(message.sid)

  #Optional: Format the SMS message like this:
  """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """
