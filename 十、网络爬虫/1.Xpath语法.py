
import requests  # 导入requests模块(发送http请求)
from lxml import html  # 导入lxml模块(解析html或xml数据)

#定义请求路径
target_url = 'https://www.tboxn.com/'

#发送请求获取响应对象
response = requests.get(target_url)

#解析html文档
"""
/: 从文档根节点查找元素
//: 从文档任意节点位置查找元素
.: 从当前节点元素下查找
meta[4]: 定位到meta标签的第4个元素
meta[last()]: 定位到meta标签的最后一个元素
meta[@name]: 定位到meta标签中含有name属性的元素
meta[@property="og:url"]: 定位到meta标签中含有property属性且属性值为og:url的元素
*: 通配符，匹配任意元素
@*: 通配符，获取标签内的所有属性值
text(): 获取标签内的文本内容
"""
doc = html.fromstring(response.text)
text = doc.xpath('/html/body/section/div/div/div/div/div[1]/div[2]/article[1]/a/div[2]/h3/b/text()')
print(text)

img = doc.xpath('//*[@id="module_id_1"]/div/div/div/div/div[2]/div[2]/article[1]/div[1]/div/a/img')
print(img)

head = doc.xpath('//head')
cnt = head[0].xpath('./meta[4]/@content')
print(cnt[0])

head = doc.xpath('//head')
cnt = head[0].xpath('./meta[last()]/@content')
print(cnt[0])

head = doc.xpath('//head')
cnt = head[0].xpath('./meta[@name]/@content')
print(cnt)

head = doc.xpath('//head')
cnt = head[0].xpath('./meta[@property="og:url"]/@content')
print(cnt)

head = doc.xpath('//head/*/div/a/img')
print(head)