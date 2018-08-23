import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from Crawler import Article



class Crawler():
    def __init__(self, url):
        print("[Crawler] initializing...")
        self.url = url
    
    def fetch_generator(self):
        i = 0

        while (not self.url == ""):
            print("[Crawler] fetching from '" + self.url + "'")
            request = requests.get(self.url)
            doc = BeautifulSoup(request.text, "html.parser")
            
            for card in doc.select(".card"):
                #print("Parsing article " + str(i))
                title = card.select(".card-title span")[1].text
                imgurl = urljoin(self.url, card.select_one("img").attrs["src"])
                text = card.select_one(".card-text").text
                emoji = card.select_one(".emoji").text
                a1 = Article(i, title, imgurl, text, emoji)
                i = i + 1
                yield a1
            
            # retrieve next page url and continue
            next_btn = doc.select_one(".navigation .btn")
            if (next_btn):
                self.url = urljoin(self.url, next_btn.attrs["href"])
                time.sleep(0.2) # sleep before accessing next page
            else:
                self.url = ""  # exit while 
    
#     def fetch(self):
#         result = []
#         i = 0
# 
#         while (not self.url == ""):
#             print("[Crawler] fetching from '" + self.url + "'")
#             request = requests.get(self.url)
#             doc = BeautifulSoup(request.text, "html.parser")
#             
#             for card in doc.select(".card"):
#                 #print("Parsing article " + str(i))
#                 title = card.select(".card-title span")[1].text
#                 imgurl = urljoin(self.url, card.select_one("img").attrs["src"])
#                 text = card.select_one(".card-text").text
#                 emoji = card.select_one(".emoji").text
#                 a1 = Article(i, title, imgurl, text, emoji)
#                 result.append(a1)
#                 i = i + 1
#             
#             # retrieve next page url and continue
#             next_btn = doc.select_one(".navigation .btn")
#             if (next_btn):
#                 self.url = urljoin(self.url, next_btn.attrs["href"])
#                 time.sleep(0.2) # sleep before accessing next page
#             else:
#                 self.url = ""  # exit while 
#             
#         return result