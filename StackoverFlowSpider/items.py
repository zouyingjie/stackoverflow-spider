# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy.loader import ItemLoader

class StackoverflowspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def add_prefix(value):
  return  'Question:' + value

class DefaultItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
class StackQuestionItem(scrapy.Item):
    # question_title = scrapy.Field()
    # question_votes = scrapy.Field()
    # question_answers = scrapy.Field()
    # question_views = scrapy.Field()
    # tags = scrapy.Field()

    # 可以定义两个字段值

    question_title = scrapy.Field(
        # 指定任意函数对值进行处理
        # input_processor = MapCompose()
        input_processor=MapCompose(add_prefix),

        # 使用 TakeFirst 来取到第一个值进行返回
        # output_processor=TakeFirst(),
    )
    question_votes = scrapy.Field(
        # output_processor=TakeFirst(),
    )
    question_answers = scrapy.Field(
        # output_processor=TakeFirst(),
    )
    question_views = scrapy.Field(
        # output_processor=TakeFirst(),
    )
    tags = scrapy.Field(
        # 通过 Join 方法可以指定分隔符来连接列表中的值
        output_processor=Join(','),
    )
