
'''






'''

import requests
import os

def getPage(kw, num):

    params = []
    for i in range(30, 30*num+30,30):
        params.append({
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': '201326592',
            'is':'',
            'fp': 'result',
            'queryWord': kw,
            'cl': '2',
            'lm': '-1',
            'ie': 'utf - 8',
            'oe': 'utf - 8',
            'adpicid':'',
            'st':'',
            'z':'',
            'ic':'',
            'hd':'',
            'latest':'',
            'copyright':'',
            'word': kw,
            's':'',
            'se':'',
            'tab':'',
            'width':'',
            'height':'',
            'face':'',
            'istype':'',
            'qc':'',
            'nc':'',
            'fr':'',
            'expermode':'',
            'force':'',
            'cg': 'girl',
            'pn': '90',
            'rn': '30',
            'gsm': '5a',
            '1590936486366':'',

        })

    url = 'https://image.baidu.com/search/acjson'
    urls = []
    for i in params:
        # 向每一个url发起请求
        res = requests.get(url=url, params=i).json()['data']
        # 获取请求数据
        urls.append(res)
    return urls

def downloadImg(datalist, dir):

    # 检测文件夹是否存在
    if not os.path.exists(dir):
        os.mkdir(dir)

    # 循环下在文件数据
    x = 0
    for data in datalist:
        for i in data:
            if i.get('thumbURL') != None:
                print(f'下载图片{i.get("thumbURL")}')
                # 发请求
                imgres = requests.get(i.get("thumbURL"))
                with open(dir+f'{x}.jpg', 'wb')as f:
                    f.write(imgres.content)
                x += 1



# 获取用户输入信息
keyword = input('请输入搜索图片的关键字：')

# 调用函数进行数据爬取 ，可指定关键字和下载页数
datalist = getPage(keyword, 2)

# 调用函数，保存数据, 可以指定要保存的图片路劲
# downloadImg(datalist,'F:\\baidu')
# 检测文件夹是否存在
if not os.path.exists('F:\\baidu'):
    os.mkdir('F:\\baidu')
    # 循环下在文件数据
x = 0
for data in datalist:
    for i in data:
        if i.get('thumbURL') != None:
            print(f'下载图片{i.get("thumbURL")}')
            # 发请求
            imgres = requests.get(i.get("thumbURL"))
            print(requests.get(i.get("thumbURL")))
            open(f'F:\\baidu\\{x}.jpg', 'wb').write(imgres.content)
            x += 1
