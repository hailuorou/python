import requests

# 目标url
url = 'http://www.rrys2019.com/user/user'

# 登陆请求的地址
loginurl = 'http://www.rrys2019.com/User/Login/ajaxLogin'

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
}

# 日过要爬虫主动记录cookie 并且携带cookie，那么使用request之前先调用session方法
# 并用返回对象请求即可

req = requests.session()

# 登陆请求数据
data = {
    'account': 'yichuan@itxdl.cn',
    'password': 'pyTHON123',
    'remember': '1',
    'url_back': 'http://www.rrys2019.com/user/user'
}

# 发起登陆请求
res = req.post(url=loginurl, headers=headers, data=data)

# 判断状态
code = res.status_code
print(code)

if code == 200:
    # 发起新的请求，去获取目标数据
    res = req.get(url=url,headers=headers)
    with open('rr.html', 'w', encoding='utf-8') as fp:
        fp.write(res.text)
