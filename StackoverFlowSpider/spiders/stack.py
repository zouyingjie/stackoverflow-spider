# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from StackoverFlowSpider.items import StackQuestionItem, DefaultItemLoader


class StackSpider(scrapy.Spider):
    name = "stack"
    allowed_domains = ["http://stackoverflow.com/"]
    start_urls = ['http://http://stackoverflow.com//']
    tag = 'python'
    url = "http://stackoverflow.com/questions/tagged/" + tag + "?page=1&sort=votes&pagesize=50"
    # 默认的解析方法，可以自己定义其他解析方法解析对应的请求
    def parse(self, response):
        html = response.text
        print(html)
        pass

    # 指定起始请求，生成一个 scrapy.Request() 请求对象
    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse_by_css)

    def parse_by_css(self, response):
        '''
        每个网页中有 50 个问题，遍历解析后存储到 mongoDB 数据库中
        :param response:
        :return:
        '''
        questions = response.css('div.question-summary')
        for question in questions:


            # 投票的数量是在 class=vote 的 div 下的 strong 中, css 通过 ::text 或者 ::attr(属性名)
            # 的方式来获取文本或者某一个属性值，因为最多只有一个值，所以直接使用 extract_first() 来获取到文本值即可
            # question_votes = question.css('.votes strong::text').extract_first()
            # # 标题是在 class=question-hyperlink 的 a 元素中
            # question_title = question.css("a.question-hyperlink::text").extract_first()
            # # 位于 class 为 answered 的 div 下的 strong 元素下
            # question_answers = question.css('.answered strong::text').extract_first()
            # # class 为 views 元素里面的 title 属性值
            # question_views = question.css('.views::attr(title)').extract_first()
            # # class 为 tags 的 div 元素下 所有 a 元素下的文本值，因为可能有多个标签，所以使用 extract() 方法，返回一个 tag 文本组成的 list
            # tags = question.css('.tags a::text').extract()
            #
            # question_item = StackQuestionItem()
            #
            # question_item["question_title"] = question_title
            # question_item["question_votes"] = question_votes
            # question_item['question_answers'] = question_answers
            # question_item['question_views'] = question_views
            # question_item['tags'] = tags

            '''
            注意：
            item 指定的是一个实例，因此要带括号
            可以指定 response 或者 selector 来确定要解析的内容，这里指定的是 selector

            解析完成后 其值去都是一个 list，为了像之前的内容那样获取到单独的值，需要作进一步的操作
            '''
            item_loader = ItemLoader(item=StackQuestionItem(),  selector=question)
            item_loader = DefaultItemLoader(item=StackQuestionItem(),  selector=question)

            item_loader.add_css('question_title', 'a.question-hyperlink::text')
            item_loader.add_css('question_votes', '.votes strong::text')
            item_loader.add_css('question_answers', '.answered strong::text')
            item_loader.add_css('question_views', '.views::attr(title)')
            item_loader.add_css('tags', '.tags a::text')

            question_item = item_loader.load_item()
            yield question_item
