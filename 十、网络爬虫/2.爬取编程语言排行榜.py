import requests
from lxml import html

dest_url = "https://www.tiobe.com/tiobe-index/"

# 发请求获取响应体对象
response = requests.get(dest_url)

# 解析响应对象中的网页文本
document = html.fromstring(response.text)

# 获取排行榜表头数据(xpath语法：可以直接在浏览器控制台导航元素中复制)
th_list = document.xpath('//*[@id="top20"]/thead/tr/th/text()')

#获取表体数据
tr_list = document.xpath('//*[@id="top20"]/tbody/tr')
td_list = []  # 存储表体数据
for tr in tr_list:
    td_list.append(tr.xpath('./td/text()'))
else:
    print(*th_list)   # 打印表头数据
    for tds in td_list:
        print(*tds)  # 打印表体数据

