# -*- coding: utf-8 -*-

# Scrapy settings for WeiboCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# -*- coding: utf-8 -*-

BOT_NAME = 'WeiboCrawler'

SPIDER_MODULES = ['WeiboCrawler.spiders']
NEWSPIDER_MODULE = 'WeiboCrawler.spiders'

ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
}

# CONCURRENT_REQUESTS 和 DOWNLOAD_DELAY 根据账号池大小调整 目前的参数是账号池大小为200

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 0.1

DOWNLOADER_MIDDLEWARES = {
    'weibo.middlewares.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
    'WeiboCrawler.middlewares.CookieMiddleware': 300,
    'WeiboCrawler.middlewares.RedirectMiddleware': 200,
    'WeiboCrawler.middlewares.IPProxyMiddleware': 100,
}

ITEM_PIPELINES = {
    'WeiboCrawler.pipelines.MongoDBPipeline': 300,
}

# MongoDb 配置

LOCAL_MONGO_HOST = '127.0.0.1'
LOCAL_MONGO_PORT = 27017
DB_NAME = 'Sina'


# IP
DOWNLOAD_TIMEOUT = 10

RETRY_TIMES = 15