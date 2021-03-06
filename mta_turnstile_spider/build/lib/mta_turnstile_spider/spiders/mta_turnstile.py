import scrapy
from mta_turnstile_spider.items import MtaTurnstileSpiderItem

class MtaTurnstile(scrapy.Spider):
    name = 'mta_turnstile'
    allowed_domains = ['web.mta.info']
    start_urls = ['http://web.mta.info/developers/turnstile.html']

    def parse(self, response):
        root_domain = 'http:/web.mta.info/developers/'

        for sel in response.xpath('//*[@id="contentbox"]/div/div/a'):
            item = MtaTurnstileSpiderItem()
            item['week_url'] = root_domain + str(sel.xpath('@href').extract()).strip("[,],'")
            request = scrapy.Request(item['week_url'], callback = self.parseTurnstileData)
            request.meta['MtaTurnstileSpiderItem'] = item
            yield request

    def parseTurnstileData(self, response):
        item = response.meta['MtaTurnstileSpiderItem']
        item = self.getTurnstileInfo(item, response)
        return item

    def getTurnstileInfo(self, item, response):
        item['turnstile_recordings'] = str(response.xpath('/html/body').extract()).split('                                        \\n')[1:]
        return item
