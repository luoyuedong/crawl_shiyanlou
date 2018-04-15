# -*- coding: utf-8 -*-
import scrapy


class CoursesFollowSpider(scrapy.Spider):
    name = 'courses_follow'
    start_urls = ['https://shiyanlou.com/courses/63']

    def parse(self, response):
        yield {
            'name': response.xpath('//h4[@class="course-infobox-title"]/span/text()').extract_first(),
            'author': response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        }
        # 从返回的 response 解析出“进阶课程”里的课程链接，依次构造
        # 请求，再将本函数指定为回调函数，类似递归
        for url in response.xpath('//div[@class="sidebox-body course-content"]/a/@href').extract():
            # 解析出的 url 是相对 url，可以手动将它构造为全 url
            # 或者使用 response.urljoin() 函数
            yield response.follow(url,callback=self.parse)
