# from random_word import Wordnik
#
# wordnik_service = Wordnik()
# print(wordnik_service.get_random_words(limit=40))


import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()


print(WORDS)