import requests
from fake_useragent import UserAgent
import time
import re
import json

un = UserAgent()

# 定义请求头
headers = {
        'User-Agent':un.random
    }

def getPage(url):
    print('getPage(url)')
    res = requests.get(url=url, headers=headers)
    if res.status_code == 200:
        return res.text
    else:
        return False


# 解析页面数据
def parseHTML(html):
    print('parseHTML(html)')
    # 获取ip地址
    try:
        reg = '<td data-title="IP">(.*)</td>'

        ip = re.findall(reg, html)

        # 获取端口号
        reg = '<td data-title="PORT">(.*)</td>'

        port = re.findall(reg, html)

        # 隐秘度
        reg = '<td data-title="匿名度">(.*)</td>'
        ym = re.findall(reg, html)

        # 类型
        reg = '<td data-title="类型">(.*)</td>'
        kind = re.findall(reg, html)

        # 最后验证时间
        reg = '<td data-title="最后验证时间">(.*)</td>'
        time = re.findall(reg, html)

        data = list(zip(ip, port, ym, kind, time))

        return data
    except:
        return False


# 测试ip是否好用
def testIp(ip):
    print('testIp(ip)')
    # 定义请求的url
    url = 'http://httpbin.org/get'

    proxies = {
        'http': f'{ip[0]}:{ip[1]}',
        'https': f'{ip[0]}:{ip[1]}'
    }
    try:
        res = requests.get(url=url, headers=headers, proxies=proxies)

        # 检测请求状态
        if res.status_code == 200:
            print('ip可用')
            return True
        else:
            print('ip不可用')
            return False
    except:
        print('ip不可用')
        return False


def main(num):
    url = 'https://www.kuaidaili.com/free/inha/'+str(num)+'/'
    # 调用页面程序
    html = getPage(url)
    if html:
        # 调用解析
        alist = parseHTML(html)
        data = []
        for ip in alist:
            # 把返回的解析数据，去发请求测试是否好用
            # okip = testIp(ip)
            # if okip:
            data.append(ip)

    # 把返回的数据写入文件
    with open('./ipdata.txt', 'a+', encoding='utf-8') as fp:
        json.dump(data, fp)


if __name__ == '__main__':
    for i in range(1,3):
        print(f'当前正在爬取第{i}页')
        main(i)
        # 每次爬取等待一段时间
        time.sleep(2)