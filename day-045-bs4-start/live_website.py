import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup)
articles = soup.select(selector=".titleline a")
article_texts = []
article_links = []
for article_tag in articles[::2]:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_num = max(article_upvotes)
print(max_num)
max_index = article_upvotes.index(max_num)
print(max_index)

print(article_texts[max_index])
print(article_links[max_index])

