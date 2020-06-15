import requests
from lxml import etree

# 封装类 进行学习猿地登路和订单获取

class LMonKey():
    # 登陆请求地址
    loginurl = 'https://www.lmonkey.com/login'
    # 账户中心地址
    orderurl = 'https://www.lmonkey.com/my/order'
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    }
    # 请求对象
    req = None
    # 请求token
    token = ''
    # 订单号
    ordercode = 0


    def __init__(self):
        # 请求对象初始化
        print('init')
        self.req = requests.session()
        self.getlogin()
        self.postlogin()
        self.getorder()

    # 登陆页面 获取下划线_token
    def getlogin(self):
        print('getlogin')
        # get请求login页面，设置cookie，获取_token
        res = self.req.get(url=self.loginurl, headers=self.headers)
        if res.status_code == 200:
            print('get登录页面请求成功')
            html = etree.HTML(res.text)
            self.token = html.xpath('//input[@name="_token"]/@value')
            print('token获取成功')
        else:
            print('请求错误')

    # post请求 提交登陆数据，进行登陆，并设置cookie
    def postlogin(self):
        uname = input('手机号：')
        passw = input('密码：')

        data = {
            '_token':self.token,
            'username':uname,
            'password':passw
        }


        # 发起post请求
        res = self.req.post(url=self.loginurl, headers=self.headers, data=data)

        if res.status_code == 200 or res.status_code == 302:
            print('登录成功')
            # 请求订单数据

    # get请求 账户中心 获取默认订单
    def getorder(self):
        res = self.req.get(url=self.orderurl, headers=self.headers)
        if res.status_code == 200:
            print('账户中心请求成功，正在解析')
            html = etree.HTML(res.text)
            r = html.xpath('//div[@class="avatar-content"]/small/text()')
            print(r)
            self.ordercode = r


obj = LMonKey()





