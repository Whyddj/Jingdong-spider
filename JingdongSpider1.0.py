import requests
import json
import pandas as pd
import time

ids = []
contents = []
times = []
# 定义三个空列表，以便保存数据

for i in range(100):  # 京东的评论最多能看到100页
        url = f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100019125569&score=0&sortType=5&page={i}&pageSize=10&isShadowSku=0&rid=0&fold=1'

        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
                'Referer': 'https://item.jd.com/100004770259.html'
        }
        # 伪装成浏览器，反反爬
        data = requests.get(url=url, headers=headers).text.lstrip('fetchJSON_comment98(').rstrip(');')
        # 保存返回的数据，去掉开头和结尾的多余部分，以变成有效的JSON字符串
        jsondata = json.loads(data)
        # 将字符串转换为Python字典
        print(f'正在爬取第{i + 1}页...')
        # 显示进度
        for x in jsondata['comments']:
                ids.append(x['id'])
                contents.append(x['content'].replace('\n', ' '))  # 将换行符替换为空格
                times.append(x['creationTime'])
        time.sleep(3)  # 停顿三秒，避免访问过快被封ip

print('正在保存为Excel文件')
df = pd.DataFrame({'用户id':ids, '评论时间':times, '评论内容':contents})
df.to_excel("output.xlsx",sheet_name='Sheet1')
print('成功！')