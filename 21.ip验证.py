
import requests
from fake_useragent import UserAgent

ua = UserAgent()

# 定义url

url = 'http://httpbin.org/get'

# 定义请求头
headers ={
    'User-Agent':ua.random
}

proxies = {
    'http':'123.207.57.145:1080',
    'https':'123.207.57.145:1080'
}

# 发起get请求
res = requests.get(url=url, headers=headers, proxies=proxies)

data = res.json()
print(data)