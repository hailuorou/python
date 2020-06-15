from lxml import etree
#
'''
/ 当前元素的直接子节点
// 当前元素的子节点或孙子节点

text()  获取文本
@attr 获取属性对应的值
'''
#
# 读取html文件并解析
html = etree.parse('./ceshi.html', etree.HTMLParser())
# print(html)  <lxml.etree._ElementTree object at 0x000001BDD0BC82C0>
# result = etree.tostring(html)
# print(result.decode('utf-8'))

r = html.xpath('/html/body/ul/li/a/text()')
# print(r)

# 获取页面中所有li里面的数据
r = html.xpath('//li/a/text()')
# print(r)


# 获取指定标签里面的li数据
r = html.xpath('//div[@class="teacher"]/ul/li/a/text()')
print(r)

h = html.xpath('//div[@class="teacher"]/ul/li/a/@href')
print(h)

res = list(zip(r, h))
print(res)