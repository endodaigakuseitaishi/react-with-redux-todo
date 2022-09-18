import requests
import time
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

yahoo_url = "https://store.shopping.yahoo.co.jp/dss/9784295000969.html?sc_i=shp_pc_search_itemlist_shsrg_title"

honto_url = "https://www.honyaclub.com/shop/g/g18550815"

def compare_product_price():
  yahoo_page = requests.get(yahoo_url)
  soup = BeautifulSoup(yahoo_page.content, "html.parser")
  # print(soup)
  product_title = soup.find(class_="mdItemName").get_text()
  product_price = soup.find(class_="elPriceNumber").get_text().replace(",", "")
  int_product_price = abs(int(product_price))
  print(int_product_price)

  honto_page = requests.get(honto_url)
  soup = BeautifulSoup(honto_page.content, "html.parser")
  item_info = soup.find(class_="item-price")
  item_price = item_info.find_all("dd")[0].get_text()[0:5].replace(",", "")
  int_item_price = abs(int(item_price))
  # real_item_price = item_price[1:6]
  # product_title = soup.find("dd")
  print(int_item_price)

  if ( int_product_price - int_item_price < 100 ):
    send_line_notify()

def send_line_notify():
  load_dotenv()
  line_notify_token = os.environ['API_TOKEN']
  line_notify_api = "https://notify-api.line.me/api/notify"
  headers = { "Authorization" : f"Bearer {line_notify_token}" }
  data = {"message": "購入検討"}
  requests.post(line_notify_api, headers=headers, data=data)
  print("通知しました")

while(True):
  print("トラッキンング")
  time.sleep(30)
  compare_product_price()
