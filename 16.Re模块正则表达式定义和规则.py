import re
'''
正则表达式规则定义
'''
# 普通字符
# vars  = 'iloveyou'
#
# reg = 'love'
# res = re.search(reg, vars).group()
# print(res)

# 转义字符 \w \W \d \D \s \S...
# \w 代表单个字母 数字 下划线
# \W代表单个的W非 字母、数字、下划线
# \d 代表单个数字
# \D代表单个的非数字
# \s代表单个空格符或制表符
# \S代表单个的非空格符或制表符
# varstr = '@_ilove  you520'
#
# reg = '\S\w\w\w\w'   # 可组合使用
# res = re.search(reg, varstr).group()
# print(res)


# 特殊字符 . * + ? {} [] () ^ $
varstr = 'hello Wor。ld  iloveyou5211'

reg = '.'    # 代表任意字符 除了换行符之外
reg = '.*'   # * 代表匹配次数 任意次数  若开始不符合直接返回
reg = '.+'   # + 代表匹配次数 至少要求匹配一次 若开始不匹配 往后跳继续匹配
reg = '.+?'  # ? 拒绝贪婪，匹配要求只要达成则返回
reg = '\w{4}' # {} 代表匹配次数 {4} 一个数字时，代表必须匹配的次数 {2，5}两个数字时，代表匹配的区间次数
reg = '[a-z]' # []代表范围
reg = '[A-Z, a-z]'
reg = '\w+(\d{4})'  # ()代表子组 括号中的表达式首先作为正则的一部分，另外会把小括号中的内容单独提取一份
reg = '(.*?)'
res = re.search(reg, varstr)
print(res.group())


varstr = '17610105211'
# 定义一个匹配手机号的正则表达式规则
reg = '^1\d{10}$'

# 定义一个正则表达式验证一个邮箱是否正确
varstr = 'zeng_c@qq.com'
reg = '[a-zA-Z0-9-_]+@[a-zA-Z0-9]+.com$'

res = re.search(reg, varstr)
# print(res.group())
# print(res.groups())

# 定义一个匹配IP的正则表达式192.168.1.1



# 正则模式
varstr = 'iloveYou'
reg = '[a-z]+'
res = re.search(reg, varstr)
# print(res.group())