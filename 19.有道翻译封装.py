
import requests
from time import sleep
import os

# 定义请求地址
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

# 定义请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
}


# 封装翻译的函数
def fanyi(kw):
    # 定义请求内容
    data = {
        'i': kw,
        'doctype': 'json',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }

    # 发送post请求
    res = requests.post(url=url, headers=headers, data=data)

    # 查看请求结果
    if res.status_code == 200:
        # print('请求成功')
        # print(res.content)
        resdata = res.json()
        if resdata['errorCode'] == 0:
            print(resdata['translateResult'][0][0]['tgt'])


vars = """
=============================
|=====欢迎使用 python 翻译=====|
|=======输入需要翻译内容========|
|==========输 q 退出==========|
=============================
    """
print(vars)

while True:

    info = input('请输入你需要翻译的内容：')

    if info == 'q':
        print('欢迎下次使用')
        break;

    fanyi(info)



