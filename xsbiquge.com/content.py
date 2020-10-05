import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://www.xsbiquge.com/15_15338/8549128.html"
    req = requests.get(url = url)
    req.encoding = "utf-8"
    # print(req.text)
    html = req.text
    bs = BeautifulSoup(html,"lxml")
    texts = bs.find('div',id='content')
    # print(texts)
    one = texts.text.strip().split('\xa0'*4)
    print(one)