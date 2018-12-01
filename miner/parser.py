from bs4 import BeautifulSoup

import requests

class Extractor:

    def __init__(self,  url):
        self.url = url

    def price(self, tag, attributes):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        return soup.find(tag, attrs=attributes).text.strip()

    def specification(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        return soup.find("table", {"class": ""})

price1 = Extractor('https://www.al.to/p/431745-smartfon-telefon-lg-g7-thinq-czarny.html').price("div", {"class": "cgNVal"})
price2 = Extractor('https://www.euro.com.pl/telefony-komorkowe/lg-g7-thinq-niebieski.bhtml').price("div", {"class": "price-normal"})
#price3 = Extractor('https://bestcena.pl/smartfony-i-telefony/lg-g7-thinq-64gb-lte-szary').price("span", {"class": "price_amount"})

print(price1, price2)