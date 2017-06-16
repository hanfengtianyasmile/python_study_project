# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanScrapyPipeline(object):
    def __init__(self):
        self.f = open('somefile.txt', 'wt', encoding='UTF-8')

    def process_item(self, item, spider):
        self.f.writelines('电影名称：' + item['title'] + '\n')
        self.f.writelines('电影介绍：' + item['movie_info'] + '\n')
        self.f.writelines('评分：' + item['star'] + '\n')
        self.f.writelines('经典话语：' + item['quote'] + '\n\n')
        return item
