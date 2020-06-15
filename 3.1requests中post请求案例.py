import requests

# 定义请求的url
url = 'https://fanyi.baidu.com/sug'

# 轻易请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
}

# 获取用户输入数据
print('请输入需要查询的单词:')
c = input()

# post发送数据
data = {'kw':c}

# 发送请求
res = requests.post(url=url, headers=headers, data=data)

# 接受返回数据
code = res.status_code
if code == 200:
    print('请求成功')
    data = res.json()
    if data['errno'] == 0:
        print('响应成功')
        print(data['data'][0]['k'])
        v = data['data'][0]['v']
        print(v.split(';')[-2])


