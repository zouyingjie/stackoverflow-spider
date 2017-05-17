# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import os
import sys

from scrapy.cmdline import execute

print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 运行命令，执行爬虫，可以使用断点进行调试
execute(['scrapy', 'crawl', 'stack'])
# execute(['scrapy', 'crawl', 'zhihu'])
# execute(['scrapy', 'crawl', 'lagou'])
