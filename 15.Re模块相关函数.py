import re

'''
re.match()函数
    特点：从头开始匹配，要么第一个就符合要求，要么不符合
         匹配成功返回match对象，否则返回None，
         返回结果可用group()获取
         可用span()获取匹配区间
re.search()函数
    特点：从字符串开头到结尾开始搜索式匹配
         匹配成功返回search对象，否则返回None，
         返回结果可用group()获取
         可用span()获取匹配区间
re.findall()
    特点：按照正则表达式规则在字符串中匹配元素，结果返回一个列表，如果没有返回空列表
re.finditer()
    特点：按照正则表达式规则在字符串中匹配所有复合规则的元素，返回一个迭代器
re.sub()
    特点：安按照正则表达式的规则，在字符串中找到需要被替换的字符串
    参数：
        pattern：正则表达式规则，匹配组要被替换的字符串
        repl：替换的字符串
        string：被替换原始字符串
compile()
    定义：可以直接将正则表达式定义为正则对象，使用正则对象直接操作
'''


# 定义字符串
vars = 'iloveyou521tosimida511'

# 定义正则表达式
reg = 'love'  # 代表一个数字

# 调用match正则方法
res = re.match(reg, vars)
# print(res)
# print(res.group())
# print(res.span())

# search
res = re.search(reg, vars)
# print(res)
# print(res.group())
# print(res.span())

# re.findall()
reg = '\d\d\d'  # 也可以 reg = '\d{3}'
# res = re.findall(reg, vars)
# print(res)

# re.finditer()
res = re.finditer(reg, vars)
# print(res)
# print(list(res))

# sub
# res = re.sub(reg, 'AAA', vars)
# print(res)

# compile
reg = re.compile('\d{3}')
res = reg.findall((vars))
print(res)

