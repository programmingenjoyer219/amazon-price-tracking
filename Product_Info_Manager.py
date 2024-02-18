from bs4 import BeautifulSoup
import requests

HEADERS = {
    "User-Agent": "YOUR-USER-AGENT",
    "Accept-Language": "YOUR-ACCEPT-LANGUAGE",
}


class ProductInfoManager:
    def __init__(self, product_url):
        self.product_url = product_url

    def get_product_info(self):
        response = requests.get(url=self.product_url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")
        product_name = soup.select_one(selector=".a-size-large .product-title-word-break").getText()
        price_whole = float(soup.find(name="span", class_="a-price-whole").getText())
        price_fraction = float(soup.find(name="span", class_="a-price-fraction").getText()) * 0.01
        net_price = price_fraction + price_whole
        return {"Product Name": product_name,
                "Net Price": net_price}
