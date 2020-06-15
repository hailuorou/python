'''
当频繁请求一个网站时，对方会认为攻击或盗取数据，禁用Ip就是反制手段
'''

import requests
from fake_useragent import UserAgent
import re
import pymysql
import sys

un = UserAgent()
while True:

    i = 1

    # 定义请求url
    url = 'https://www.kuaidaili.com/free/inha/'+str(i)+'/'


    if i >= 20:
        break

    # 定义请求头
    headers = {
        'User-Agent':un.random
    }


    # 发起get请求
    res = requests.get(url=url, headers=headers)

    if res.status_code == 200:
        print('请求成功')

        # 获取ip地址
        reg = '<td data-title="IP">(.*)</td>'

        ip = re.findall(reg,res.text)

        # 获取端口号
        reg = '<td data-title="PORT">(.*)</td>'

        port = re.findall(reg, res.text)

        # 隐秘度
        reg = '<td data-title="匿名度">(.*)</td>'
        ym = re.findall(reg, res.text)

        # 类型
        reg = '<td data-title="类型">(.*)</td>'
        kind  = re.findall(reg, res.text)

        # 最后验证时间
        reg = '<td data-title="最后验证时间">(.*)</td>'
        time = re.findall(reg, res.text)


        # 将数据写入数据库
        try:
            conn = pymysql.connect(host="127.0.0.1", user='root', port=3306, passwd='root', db='db1', charset='utf8')
            cursor = conn.cursor()

            insert_inf = ("insert into dlip(ip, port, ym, kind, time)" "values (%s, %s, %s, %s, %s)")
            for i in range(len(ip)):
                data_inf = (ip[i], port[i], ym[i], kind[i],time[i])
                cursor.execute(insert_inf, data_inf)
            conn.commit()

            conn.close()

        except :
            s = sys.exc_info()
            print("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))
            print('connect mysql error.')

