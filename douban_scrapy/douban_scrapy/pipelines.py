# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanScrapyPipeline(object):
    def __init__(self):
        self.f = open('somefile.txt', 'wt', encoding='UTF-8')

    def process_item(self, item, spider):
        self.f.writelines('回帖时间：' + item['title'] + '\n')
        self.f.writelines('回帖内容：' + item['movie_info'] + '\n')
        self.f.writelines('回帖人：' + item['star'] + '\n\n')
        self.f.writelines('回帖人：' + item['star'] + '\n\n')
        return item
