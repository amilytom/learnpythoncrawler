import requests        #导入requests包
from bs4 import BeautifulSoup
url='http://www.cntour.cn/'
strhtml=requests.get(url)
soup=BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
print(data)

import re
for item in data:
    result={
        "title":item.get_text(),
        "link":item.get('href'),
        'ID':re.findall('\d+',item.get('href'))
    }
print(result)