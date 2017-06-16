from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from douban_scrapy.items import DoubanScrapyItem
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class Douban(CrawlSpider):

    name = 'douban'

    start_urls = ['https://movie.douban.com/top250']

    url = 'https://movie.douban.com/top250'

    def parse(self, response):

        item = DoubanScrapyItem()
        selector = Selector(response)

        movies = selector.xpath('//div[@class="info"]')

        for movie in movies:

            title = movie.xpath('div[@class="hd"]/a/span/text()').extract()

            full_title = ''.join(title)

            movie_info = movie.xpath('div[@class="bd"]/p/text()').extract()[0].strip()

            star = movie.xpath('div[@class="bd"]/div/span[@class="rating_num"]/text()').extract()[0]

            quote = movie.xpath('div[@class="bd"]/p/span[@class="inq"]/text()').extract()
            #这里要判断，否则爬虫会在这里卡住
            if not quote:
                quote = ''
            else:
                quote = quote[0]

            item['title'] = full_title
            item['movie_info'] = movie_info
            item['star'] = star
            item['quote'] = quote

            yield item

        next_link = selector.xpath('//span[@class="next"]/a/@href').extract()

        if next_link:
            next_link = next_link[0]
            yield Request(self.url + next_link, callback=self.parse)

