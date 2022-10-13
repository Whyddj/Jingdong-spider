# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql  # 导入第三方库


class JingdongspiderPipeline:
    def process_item(self, item, spider):
        return item


class DpPipeline:
    # 创建DpPipeline类，在这个类中写对数据进行处理的方法，即保存到数据库

    def __init__(self):
        # 定义初始化方法
        self.conn = pymysql.connect(host='localhost', port=3306,
                                    user='root', password='Wang123abc',
                                    database='JD', charset='utf8mb4')
        # 连接本地数据库，把链接对象绑定到self上
        self.cursor = self.conn.cursor()
        # 获取游标

    def close_spider(self, spider):
        # 当关闭爬虫时，要执行的代码
        self.cursor.close()
        self.conn.close()
        # 释放游标,断开连接

    def process_item(self, item, spider):
        # 当拿到数据时，要执行的代码
        id = item.get('a_id', '')
        time = item.get('b_time', '')
        comment = item.get('c_comment', '')
        # 从item中拿到数据
        self.cursor.execute(
            'INSERT INTO comments (id, comment_time, content) values(%s, %s, %s)',
            (id, time, comment)
        )
        # 通过游标执行INSERT语句
        self.conn.commit()
        # 用commit方法提交确认
        return item
