import requests
import json
from lxml import etree

# 请求地址
url = 'https://www.lmonkey.com/essence'

# 请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
}

# 发送get请求
res = requests.get(url=url, headers=headers)

# 请求成功
if res.status_code==200:
    # 请求内容写入文件
    with open('./yuanzhu.html', 'w', encoding='utf-8') as fp:
        fp.write(res.text)

# 解析数据
html = etree.parse('./yuanzhu.html', etree.HTMLParser())

# 提取数据 作者 文章标题 文章地址url
# author = html.xpath('//div[contains(@class,"old_content")]//div[contains(@class,"list-group-item")]//strong/a/text()')
author = html.xpath('//div[@class="list-group-item list-group-item-action px-0 xin_hover"]//strong/a/text()')
titles = html.xpath('//div[@class="topic_title mb-0  essence_title yh"]/text()')
titleurl = html.xpath('//div[@class="flex-fill  col-12 col-md-8 px-3 px-md-0 pt-2 pt-md-0"]/a[1]/@href')

# print(len(author))
# print(len(titles))
# print(titleurl)
# print(len(titleurl))

# res = zip(author, titles, titleurl)
# print(list(res))

data = []
for i in range(0,len(author)):
    res = {'作者：':author[i], '标题：':titles[i], '文章链接：':titleurl[i]}
    data.append(res)

print(data)


# 写入数据
with open('./yz.json', 'w') as fp:
    json.dump(data, fp)

