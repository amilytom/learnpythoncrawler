#!/usr/bin/python
import requests        #导入requests包
import json
def get_translate_date(word=None):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
               'Cookie':'OUTFOX_SEARCH_USER_ID=-1746384715@10.169.0.84; JSESSIONID=aaa5eAuqfBxPmeDXOxYtx; OUTFOX_SEARCH_USER_ID_NCOO=536723350.2714234; ___rl__test__cookies=1601793988857',
               'Referer':'http://fanyi.youdao.com/'
               }
    #response = requests.get(url, headers=headers)
    # From_data={'i':word,'from':'zh-CHS','to':'en','smartresult':'dict','client':'fanyideskweb','salt':'15477056211258','sign':'b3589f32c38bc9e3876a570b8a992604','ts':'1547705621125','bv':'b33a2f3f9d09bde064c9275bcb33d94e','doctype':'json','version':'2.1','keyfrom':'fanyi.web','action':'FY_BY_REALTIME','typoResult':'false'}
    From_data={'i':word,'from': 'AUT','to': 'AUTO','smartresult': 'dict','client': 'fanyideskweb','salt': '16017939888595','sign': 'ee59b49d17a0a2d713f2159396ac44bc','lts': '1601793988859','bv': 'acc97416ef67184f42e5a4a03c3d52ab','doctype': 'json','version': '2.1','keyfrom': 'fanyi.web','action': 'FY_BY_REALTlME'}

    #请求表单数据
    response = requests.post(url,headers=headers,data=From_data)
    #将Json格式字符串转字典
    content = json.loads(response.text)
    print(content)
    #打印翻译后的数据
    print(content['translateResult'][0][0]['tgt'])
if __name__=='__main__':
    get_translate_date('我爱中国')