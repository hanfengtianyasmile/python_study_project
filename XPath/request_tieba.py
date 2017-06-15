#使用XPath，百度贴吧爬虫

from multiprocessing.dummy import Pool as ThreadPool
from lxml import etree
import requests
import json


def wirteContent(content_dict, f):
    f.writelines('回帖时间：'+content_dict['reply_time'] + '\n')
    f.writelines('回帖内容：'+content_dict['reply_content'] + '\n')
    f.writelines('回帖人：'+content_dict['reply_user'] + '\n\n')

def spider(url):

    html = requests.get(url)
    selector = etree.HTML(html.text)
    content_field = selector.xpath('//div[@class="l_post j_l_post l_post_bright  "]')
    item = {}


    for each in content_field:

        reply_info = json.loads(each.xpath('@data-field')[0])
        reply_user = reply_info['author']['user_name']
        reply_time = reply_info['content']['date']
        reply_content = each.xpath('div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content  clearfix"]/text()')[0].strip()

        item['reply_content'] = reply_content
        item['reply_user'] = reply_user
        item['reply_time'] = reply_time

        wirteContent(item, f)



if __name__ == '__main__':
    #多线程,默认几核就传几个线程
    pool = ThreadPool(4)

    #默认字符编码为gbk，但是获取的网页内容为utf-8编码，所以要统一编码
    f = open('somefile.txt', 'wt', encoding='UTF-8')

    page = []

    for i in range(1,21):
        newpage = 'http://tieba.baidu.com/p/3742662820?pn='+str(i)
        page.append(newpage)

    #传递要执行的函数，函数参数(可遍历)
    pool.map(spider, page)
    pool.close()
    pool.join()




