# -*- coding: utf-8 -*-

# Scrapy settings for Danmarkprice project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import scrapy_redis
import datetime

BOT_NAME = 'Danmarkprice'

SPIDER_MODULES = ['Danmarkprice.spiders']
NEWSPIDER_MODULE = 'Danmarkprice.spiders'

# HTTPERROR_ALLOWED_CODES=[500]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Danmarkprice (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Danmarkprice.middlewares.DanmarkpriceSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Danmarkprice.middlewares.DanmarkpriceDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Danmarkprice.pipelines.DanmarkpricePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# MongoDB设置
MONGO_URI = 'mongodb://192.168.0.233:27017'
# MONGO_URI = 'mongodb://192.168.0.100:27017'
MONGO_DB = "Danmark"
MONGO_COLL = 'Danmark_price'

# 日志文件
LOG_LEVEL = 'WARNING'
log_name = 'Danmark_price' + datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S') + '.log'
LOG_FILE = log_name

# 使用scrapy-redis里的去重组件，不使用scrapy默认的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy-redis里的调度器组件，不使用scrapy默认的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 允许暂停，redis请求记录不丢失
SCHEDULER_PERSIST = True
REDIS_HOST = '127.0.0.1'
# REDIS_HOST = '192.168.0.100'
REDIS_PORT = 6379
# REDIS_PARAMS = {'password': '123'}
REDIS_PARAMS = {'password': 'jianshu2018'}

#开启代理中间件
DOWNLOADER_MIDDLEWARES={
    # 'Danmarkprice.middlewares.ProxyMiddleware':544,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 300,
    'Danmarkprice.middlewares.RandomUserAgentMiddleware': 543,
}
#代理IP池
IPPOOL=[
{"ipaddr":"80.211.36.44:8080"},
{"ipaddr":"80.211.159.187:80"},
{"ipaddr":"80.211.36.44:3128"},
{"ipaddr":"80.211.68.29:8080"},
{"ipaddr":"80.211.234.18:80"},
{"ipaddr":"80.211.36.44:80"},
{"ipaddr":"80.211.234.18:8080"}
]

