from bs4 import BeautifulSoup


html_doc = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>学习猿地 - 成就自己的只需一套精品</title>
</head>
<body>
    <p class ="title">内容如下</p>
    <a href="/a/b/c/java">Java工程师</a>
    <p>Java在当前比较火值得学习</p>
    <a href="/a/b/c/python">python工程师</a>
    <p>python写爬虫很棒</p>
    <a href="/a/b/c/ai">AI工程师</a>
    <p>ai改变世界</p>
    
</body>
'''

# 创建一个BeautifulSoup对象，建议手动指定解析器
soup = BeautifulSoup(html_doc, 'lxml')

# 通过tag标签对象获取文档数据
r = soup.title
r = soup.title.text  # 获取文本
# print(r)

p = soup.p
# print(p)

# 通过搜索获取页面中的元素 find, find_all

r = soup.find('a')
# print(r)
r = soup.find_all('a')
# print(r)

# css选择器

# 通过标签选择元素
r = soup.select('title')
# print(r)

# 通过class类获取元素
r = soup.select('.title')
# print(r)

# 通过ID名获取元素

# 通过空格 层级关系获取元素
r = soup.select('html body p')
print(r)
# 通过逗号 并列关系获取元素
r = soup.select('title, a')
# print(r)
