import requests

# 定义请求的url
url = 'https://www.baidu.com'

# 发起get请求
res = requests.get(url=url)

# 获取响应结果
print(res)    # <Response [200]> 对象
print(res.content)  # b'...' 二进制文本流
print(res.content.decode('utf-8'))  # 把二进制文本流按utf-8转换为普通字符集
print(res.text)  # 获取相应内容
print(res.status_code)  # 请求状态码 200代表成功
print(res.url)  # 请求url
print(res.request.headers)  # 请求头信息
print(res.headers)  # 响应头信息

