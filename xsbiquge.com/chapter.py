import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    sever = 'https://www.xsbiquge.com'
    target = 'https://www.xsbiquge.com/15_15338/'

    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    bs = BeautifulSoup(html,'lxml')
    # chapters = bs.find('div',id='list')
    chapters = bs.select('#list>dl>dd>a')
    # print(chapters)
    for chapter in chapters:
        url = chapter.get('href')
        print(chapter.string)
        print(sever + url)

