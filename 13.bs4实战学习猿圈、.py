import requests
from bs4 import BeautifulSoup
import json

# 定义请求url
url = 'https://www.lmonkey.com/t'

# 定义请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
}

res = requests.get(url=url, headers=headers)

# 判断是否成功并获取源码
if res.status_code == 200:
    print('请求成功')

    # 解析数据
    soup = BeautifulSoup(res.text, 'lxml')

    # 获取数据
    # 获取文章大div
    divs = soup.find_all('div', class_="list-group-item list-group-item-action p-06")
    varlist = []
    for i in divs:
        r = i.find('div', class_="topic_title mb-0 lh-180")
        if r:
            # i.p.span.text.split('\n')[1].replace(' ','')
            vardict = {'title：': r.text.split('\n')[0],
                       'url：': i.a['href'],
                       'author：': i.p.strong.a.text,
                       'time：': i.p.span['title']
                       }
            varlist.append(vardict)
    print(varlist)

    # 写入数据
    with open('./yq.json', 'w', encoding='utf-8') as fp:
        json.dump(varlist, fp)
