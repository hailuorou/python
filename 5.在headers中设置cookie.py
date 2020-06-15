import requests

# 定义请求的url
url = 'https://www.bilibili.com/'


# 定义请求头信息
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'

}

# 发起get请求
res = requests.get(url=url, headers=headers)

# 获取响应状态码
code = res.status_code
print(code)

if code == 200:
    with open('./test2.html', 'w', encoding='utf-8') as fp:
        fp.write(res.text)
