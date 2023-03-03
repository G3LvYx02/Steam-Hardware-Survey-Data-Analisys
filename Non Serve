import scrapy

class SteamSpider(scrapy.Spider):
    name = 'steam'
    start_urls = ['https://store.steampowered.com/hwsurvey/']

    def parse(self, response):
        for row in response.xpath('//table[@class="survey"]/tr'):
            yield {
                'os': row.xpath('td[1]/text()').get(),
                'cpu': row.xpath('td[2]/text()').get(),
                'gpu': row.xpath('td[3]/text()').get(),
                'ram': row.xpath('td[4]/text()').get(),
                'display': row.xpath('td[5]/text()').get(),
                'primary_display_res': row.xpath('td[6]/text()').get(),
                'secondary_display_res': row.xpath('td[7]/text()').get(),
                'dx_version': row.xpath('td[8]/text()').get(),
                'vram': row.xpath('td[9]/text()').get(),
                'storage': row.xpath('td[10]/text()').get(),
                'steam_controller': row.xpath('td[11]/text()').get(),
                'headset': row.xpath('td[12]/text()').get(),
            }

        next_page = response.xpath('//div[@class="pageLinks"]/a[@class="next"]/@href')
        if next_page:
            yield response.follow(next_page[0], self.parse)

