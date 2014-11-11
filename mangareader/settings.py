# -*- coding: utf-8 -*-

# Scrapy settings for mangareader project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mangareader'

SPIDER_MODULES = ['mangareader.spiders']
NEWSPIDER_MODULE = 'mangareader.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'mangareader (+http://www.yourdomain.com)'


LOG_LEVEL = 'DEBUG'
ITEM_PIPELINES = {
    'mangareader.pipelines.DownloadPicCoverPipeline': 1,
}

IMAGES_EXPIRES = 90
IMAGES_STORE = '/data/program/mangareader/picdown/'
