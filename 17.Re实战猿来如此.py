'''
数据地址：https://www.lmonkey.com/ask
数据字段：问题 时间 作者
'''
import sys

import requests
import re
import pymysql

# 定义url
url = 'https://www.lmonkey.com/ask'

# 定义请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
}

# 发送get请求
res = requests.get(url=url, headers=headers)

# 判断状态并判断是否成功
if res.status_code == 200:
    print('请求成功')
    # 获取返回数据
    res_html = res.text
    # 进行数据解析

    # 定义解析问题标题的正则
    reg = '<div class="topic_title mb-0 lh-180 ml-n2">(.*)<small'

    titlelist = re.findall(reg, res_html)

    # 定义解析时间正则
    reg = ' <span data-toggle="tooltip" data-placement="top" title="(.*)">'
    timelist = re.findall(reg, res_html)

    # 定义解析作者正则
    reg = '<strong>(.*)</strong>'
    authorlist = re.findall(reg, res_html)

    # 定义文章链接正则
    reg = '<a href="https://(www.lmonkey.com/ask/\d*)" target="_blank">'
    urllist = re.findall(reg, res_html)

    # 将数据写入数据库
    try:
        conn = pymysql.connect(host="127.0.0.1", user='root', port=3306, passwd='root', db='db1', charset='utf8')
        cursor = conn.cursor()

        sql = """
                create table ylrc(
                title varchar(1000),
                author varchar(20),
                time varchar(1000),
                url varchar(1000))
              """


        cursor.execute(sql)
        conn.commit()

        cursor = conn.cursor()
        insert_inf = ("insert into ylrc(title, author, time,url)" "values (%s, %s, %s, %s)")
        for i in range(len(titlelist)):
            data_inf = (titlelist[i], authorlist[i], timelist[i], urllist[i])
            cursor.execute(insert_inf, data_inf)
        conn.commit()

        conn.close()

    except :
        s = sys.exc_info()
        print("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))
        print('connect mysql error.')


